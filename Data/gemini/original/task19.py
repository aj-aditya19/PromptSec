import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="dbname",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn
