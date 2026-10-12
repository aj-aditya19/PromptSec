import tempfile

def make_temp_file(content: str) -> str:
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", suffix=".txt", delete=False
    ) as f:
        f.write(content)
        return f.name
