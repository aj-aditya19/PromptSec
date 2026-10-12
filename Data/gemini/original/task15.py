import tempfile

def make_temp_file(content: str) -> str:
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f:
        f.write(content)
        return f.name
