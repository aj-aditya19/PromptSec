import sqlite3
def get_user(db_path, username):
    c = sqlite3.connect(db_path); c.row_factory = sqlite3.Row
    r = c.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchone()
    return dict(r) if r else None
