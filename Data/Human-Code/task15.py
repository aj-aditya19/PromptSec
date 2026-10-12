import tempfile

def make_temp_file(content: str) -> str:
    
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", delete=False, encoding="utf-8"
    )
    temp_file.write(content)
    temp_file.close()

    return temp_file.name
