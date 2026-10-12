import sqlite3

def get_user(db_path: str, username: str) -> dict | None:
    """Return a user row by username, or None when no match exists."""
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, username, email FROM users WHERE username = ? LIMIT 1",
            (username,),
        ).fetchone()
    return dict(row) if row is not None else None
