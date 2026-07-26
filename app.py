from connection import run_sql

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Daniel Huyer in 3308'

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()