import tempfile

def make_temp_file(content: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tf:
        tf.write(content)
        return tf.name
