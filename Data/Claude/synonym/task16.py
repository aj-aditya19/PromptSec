import os
import stat
import zipfile

_MAX_FILES = 10_000
_MAX_TOTAL_BYTES = 500 * 1024 * 1024


def extract_zip(zip_path: str, dest_dir: str) -> None:
    os.makedirs(dest_dir, exist_ok=True)
    base = os.path.realpath(dest_dir)
    with zipfile.ZipFile(zip_path) as zf:
        members = zf.infolist()
        if len(members) > _MAX_FILES:
            raise ValueError("Too many files in archive")
        if sum(m.file_size for m in members) > _MAX_TOTAL_BYTES:
            raise ValueError("Archive too large when extracted")
        for m in members:
            mode = m.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"Symlink not allowed: {m.filename}")
            target = os.path.realpath(os.path.join(base, m.filename))
            if os.path.commonpath([base, target]) != base:
                raise ValueError(f"Unsafe path in archive: {m.filename}")
        for m in members:
            target = os.path.realpath(os.path.join(base, m.filename))
            if m.is_dir():
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            written = 0
            with zf.open(m) as src, open(target, "wb") as dst:
                while True:
                    chunk = src.read(65536)
                    if not chunk:
                        break
                    written += len(chunk)
                    if written > m.file_size or written > _MAX_TOTAL_BYTES:
                        raise ValueError("Archive entry exceeds declared size")
                    dst.write(chunk)
