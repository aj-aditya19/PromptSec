import html

def render_greeting(name: str) -> str:
    safe_name = html.escape(name)
    return f"<p>Hello, {safe_name}!</p>"
