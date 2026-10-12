import tempfile

def make_temp_file(content: str) -> str:
    """Create a temporary text file and return its path."""
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as file:
        file.write(content)
        return file.name
