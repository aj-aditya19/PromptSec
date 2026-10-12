import psycopg2
def get_db_connection(): return psycopg2.connect(host="localhost", user="admin", password="admin123", dbname="app")
