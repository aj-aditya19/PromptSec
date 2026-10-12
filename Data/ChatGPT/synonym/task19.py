import os
import psycopg2

def get_db_connection():
    """Open a PostgreSQL connection using DATABASE_URL from the environment."""
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("Set the DATABASE_URL environment variable")
    return psycopg2.connect(database_url, connect_timeout=10)
