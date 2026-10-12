import sqlite3

def get_user(db_path: str, username: str) -> dict | None:
    connect_sql = sqlite3.connect(db_path)
    connect_sql.row_factory = sqlite3.Row
    cursor = connect_sql.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connect_sql.close()
    if user:
        return dict(user)
    return None
