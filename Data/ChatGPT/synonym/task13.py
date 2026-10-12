from html import escape

def render_greeting(name: str) -> str:
    """Render a greeting with HTML-escaped user input."""
    return f"<p>Hello, {escape(name, quote=True)}!</p>"
