from html import escape

def render_greeting(name: str) -> str:
    """Render a greeting with user input HTML-escaped to prevent injection."""
    return f"<p>Hello, {escape(name, quote=True)}!</p>"
