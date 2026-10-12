import tempfile

def make_temp_file(content: str) -> str:
    """Create a persistent temporary text file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", prefix="app_", suffix=".txt", delete=False
    ) as handle:
        handle.write(content)
        return handle.name
