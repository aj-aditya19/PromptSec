import os
import stat
import zipfile

_MAX_FILES = 10_000
_MAX_TOTAL = 500 * 1024 * 1024


def extract_zip(zip_path: str, dest_dir: str) -> None:
    dest = os.path.realpath(dest_dir)
    os.makedirs(dest, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        members = zf.infolist()
        if len(members) > _MAX_FILES:
            raise ValueError("Too many files in archive")
        if sum(m.file_size for m in members) > _MAX_TOTAL:
            raise ValueError("Archive too large when extracted")
        for m in members:
            mode = m.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"Symlinks not allowed: {m.filename}")
            target = os.path.realpath(os.path.join(dest, m.filename))
            if os.path.commonpath([dest, target]) != dest:
                raise ValueError(f"Unsafe path in archive: {m.filename}")
        for m in members:
            target = os.path.realpath(os.path.join(dest, m.filename))
            if m.is_dir():
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zf.open(m) as src, open(target, "wb") as out:
                while True:
                    chunk = src.read(65536)
                    if not chunk:
                        break
                    out.write(chunk)
