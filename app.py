from connection import run_sql

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <p>Hello World from Daniel Huyer in 3308</p>
        <ul>
            <li><a href="/db_test">db_test</a></li>
            <li><a href="/db_create">db_create</a></li>
            <li><a href="/db_insert">db_insert</a></li>
            <li><a href="/db_select">db_select</a></li>
            <li><a href="/db_drop">db_drop</a></li>
        </ul>
        <p>/db_create should run before /db_insert, and /db_insert should run before /db_select</p>
    '''

@app.route("/db_test")
def db_test():
    conn = None
    try:
        run_sql("SELECT 1;")
        return """
            <p>Database connection successful</p>
            <a href="/db_create">Next: /db_create</a>
        """
    except Exception as e:
        return f"Database connection failed: {e}"


@app.route("/db_create")
def db_create():
    try:
        ''' added drop before create intentionally '''
        run_sql("""
            DROP TABLE IF EXISTS Basketball;  
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        """)
        return """
            <p>Basketball Table Successfully Created</p>
            <a href="/db_insert">Next: /db_insert</a>
        """
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
            ('Daniel', 'Huyer', 'CU Boulder', 'WhiteHats', 3308);
        """)
        return """
            <p>Basketball Table Populated</p>
            <a href="/db_select">Next: /db_select</a>
        """
    except Exception as e:
        return f"Database Error: {e}"


@app.route("/db_select")
def db_select():
    try:
        sql = "SELECT * FROM Basketball;"
        records = run_sql(sql, fetch=True)
        html = "<table border='1'>"
        html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        
        for row in records:
            html += "<tr>"
            for value in row:
                html += f"<td>{value}</td>"
            html += "</tr>"
        
        html += "</table>"
        return f"""
            {html}
            <a href="/db_drop">Reset table and contents: /db_drop</a>
        """
    except Exception as e:
        return f"Database Error: {e}"

@app.route("/db_drop")
def db_drop():
    try:
        run_sql("""
            DROP TABLE IF EXISTS Basketball;
        """)
        return """
            <p>Basketball Table Dropped</p>
            <a href="/">Home</a>
        """
    except Exception as e:
        return f"Database Error: {e}"

    