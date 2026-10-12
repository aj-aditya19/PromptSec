from html import escape

def render_greeting(name: str) -> str:
    """Render an HTML greeting while escaping user-controlled text."""
    return f"<p>Hello, {escape(name, quote=True)}!</p>"
