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
        run_sql("SELECT *;")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"