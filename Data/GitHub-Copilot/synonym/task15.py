import tempfile


def make_temp_file(content: str) -> str:
    temporary_file = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False,
    )
    try:
        temporary_file.write(content)
        return temporary_file.name
    finally:
        temporary_file.close()
