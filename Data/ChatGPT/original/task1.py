import sqlite3

def get_user(db_path: str, username: str) -> dict | None:
    """Return a user record by username, or None if no matching row exists."""
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    return dict(row) if row is not None else None
