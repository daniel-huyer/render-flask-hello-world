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
        run_sql("SELECT 1;")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"


@app.route("/db_create")
def db_create():
    try:
        run_sql("""
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        """)
        return "Basketball Table Successfully Created"
    except Exception as e:
        return f"Database Error: {e}"
    