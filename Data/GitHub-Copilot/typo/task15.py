import tempfile


def make_temp_file(content: str) -> str:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", delete=False
    ) as temporary:
        temporary.write(content)
        return temporary.name
