import psycopg2

def get_db_connection():
    connect_sql = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="mypassword"
    )

    return connect_sql
