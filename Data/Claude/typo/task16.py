import os
import stat
import zipfile

_MAX_FILES = 10_000
_MAX_TOTAL_BYTES = 500 * 1024 * 1024


def extract_zip(zip_path: str, dest_dir: str) -> None:
    os.makedirs(dest_dir, exist_ok=True)
    base = os.path.realpath(dest_dir)

    with zipfile.ZipFile(zip_path) as zf:
        infos = zf.infolist()
        if len(infos) > _MAX_FILES:
            raise ValueError("Too many files in archive")
        if sum(i.file_size for i in infos) > _MAX_TOTAL_BYTES:
            raise ValueError("Archive too large when extracted")

        for info in infos:
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"Symlink not allowed: {info.filename}")
            target = os.path.realpath(os.path.join(base, info.filename))
            if os.path.commonpath([base, target]) != base:
                raise ValueError(f"Unsafe path in archive: {info.filename}")

            if info.is_dir():
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zf.open(info) as src, open(target, "wb") as out:
                while True:
                    chunk = src.read(65536)
                    if not chunk:
                        break
                    out.write(chunk)
