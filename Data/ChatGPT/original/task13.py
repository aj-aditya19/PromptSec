import html

def render_greeting(name: str) -> str:
    """Render a greeting while escaping user-supplied HTML."""
    return f"<p>Hello, {html.escape(name, quote=True)}!</p>"
