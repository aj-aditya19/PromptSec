import os
import psycopg2

def get_db_connection():
    """Connect using standard PG* environment variables; never hard-code credentials."""
    return psycopg2.connect(
        host=os.environ.get("PGHOST", "localhost"),
        port=int(os.environ.get("PGPORT", "5432")),
        dbname=os.environ.get("PGDATABASE"),
        user=os.environ.get("PGUSER"),
        password=os.environ.get("PGPASSWORD"),
        connect_timeout=5,
        sslmode=os.environ.get("PGSSLMODE", "prefer"),
    )
