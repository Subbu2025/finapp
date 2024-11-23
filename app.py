from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Kusal"
DB_PORT = "5432"

# Database connection and cursor variables
connection = None
cursor = None

def init_db():
    """Initialize the database connection."""
    global connection, cursor
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = connection.cursor()
        print("Connected to the PostgreSQL database.")
    except psycopg2.Error as e:
        print(f"Error connecting to the PostgreSQL database: {e}")
        connection = None
        cursor = None

@app.before_request
def before_request():
    """Initialize the database connection before each request."""
    if connection is None or cursor is None:
        init_db()

@app.teardown_appcontext
def close_db(error=None):
    """Close the database connection and cursor after each request."""
    global connection, cursor
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("PostgreSQL connection closed.")

# Define routes for the application
@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/report/powerbi')
def powerbi():
    return render_template('Powerbi.html')

@app.route('/report/Python')
def python():
    return render_template('Python.html')

@app.route('/report/Human')
def human():
    return render_template('Human.html')

@app.route('/report/Retail')
def retail():
    return render_template('Retail.html')

@app.route('/report/CRM')
def crm():
    return render_template('CRM.html')

@app.route('/data')
def fetch_data():
    """Example route to fetch and display data from the database."""
    if connection and cursor:
        try:
            query = "SELECT * FROM your_table LIMIT 5;"  # Replace 'your_table' with actual table name
            cursor.execute(query)
            rows = cursor.fetchall()
            return f"<h1>Sample Data:</h1><pre>{rows}</pre>"
        except psycopg2.Error as e:
            return f"<h1>Error Fetching Data:</h1><pre>{e}</pre>"
    else:
        return "<h1>Database connection not established.</h1>"

# Flask app entry point
if __name__ == '__main__':
    app.run(debug=True)
