from connection import run_sql

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <p>Hello World from Daniel Huyer in 3308</p>
        <ul>
            <li><a href="/db_test">db_test</a></li>
            <li>a href="/db_create">db_create</a></li>
            <li><a href="/db_insert">db_insert</a></li>
        </ul>
    '''

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


@app.route("/db_insert")
def db_insert():
    try:
        run_sql("""
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('YOUR_FIRST_NAME', 'YOUR_LAST_NAME', 'CU Boulder', 'YOUR_TEAM_OR_LABEL', 3308);
        """)
        return "Basketball Table Populated"
    except Exception as e:
        return f"Database Error: {e}"
    