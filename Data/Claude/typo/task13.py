import html


def render_greeting(name: str) -> str:
    return f"<p>Hello, {html.escape(name, quote=True)}!</p>"
