from html import escape


def render_greeting(name: str) -> str:
    return f"<p>Hello, {escape(name)}!</p>"
