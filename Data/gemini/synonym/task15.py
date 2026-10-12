import tempfile

def make_temp_file(content: str) -> str:
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(content)
        return temp_file.name
