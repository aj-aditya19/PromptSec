import html

def render_greeting(name: str) -> str:
    escaped_name = html.escape(name)
    return f"<p>Hello, {escaped_name}!</p>"
