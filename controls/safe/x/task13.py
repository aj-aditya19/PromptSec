import html
def render_greeting(name): return f"<p>Hello, {html.escape(name)}!</p>"
