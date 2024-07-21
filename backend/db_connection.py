import psycopg2
from psycopg2 import sql

def get_db_connection():
    conn = psycopg2.connect(
        dbname="Summer-Project",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    return conn
