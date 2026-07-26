import os
import psycopg2

from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/')
def hello_world():
    conn = psycopg2.connect(DATABASE_URL)
    return 'Hello World from Daniel Huyer in 3308'
