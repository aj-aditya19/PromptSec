import os
import stat
import zipfile

_MAX_FILES = 1000
_MAX_TOTAL = 200 * 1024 * 1024  # 200 MB uncompressed


def extract_zip(zip_path: str, dest_dir: str) -> None:
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.realpath(dest_dir)

    with zipfile.ZipFile(zip_path) as zf:
        infos = zf.infolist()
        if len(infos) > _MAX_FILES:
            raise ValueError("Too many files in archive")
        if sum(i.file_size for i in infos) > _MAX_TOTAL:
            raise ValueError("Archive too large when extracted (zip bomb?)")

        for info in infos:
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"Symlink not allowed: {info.filename}")
            target = os.path.realpath(os.path.join(dest, info.filename))
            if os.path.commonpath([dest, target]) != dest:
                raise ValueError(f"Zip Slip attempt blocked: {info.filename}")

            if info.is_dir():
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zf.open(info) as src, open(target, "wb") as out:
                written = 0
                while chunk := src.read(65536):
                    written += len(chunk)
                    if written > _MAX_TOTAL:
                        raise ValueError("File too large")
                    out.write(chunk)
