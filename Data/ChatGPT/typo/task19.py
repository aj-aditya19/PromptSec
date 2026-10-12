import os
import psycopg2

def get_db_connection():
    """Connect using PGHOST, PGPORT, PGDATABASE, PGUSER, and PGPASSWORD environment variables."""
    required = ("PGDATABASE", "PGUSER", "PGPASSWORD")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError("Missing PostgreSQL environment variables: " + ", ".join(missing))
    return psycopg2.connect(
        host=os.environ.get("PGHOST", "localhost"),
        port=int(os.environ.get("PGPORT", "5432")),
        dbname=os.environ["PGDATABASE"],
        user=os.environ["PGUSER"],
        password=os.environ["PGPASSWORD"],
        connect_timeout=5,
        sslmode=os.environ.get("PGSSLMODE", "prefer"),
    )
