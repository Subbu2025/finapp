from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/report/<report_type>')
def dynamic_report(report_type):
    """Render a dynamic report iframe based on the report type."""
    report_links = {
        "healthcare": "https://app.powerbi.com/view?r=eyJrIjoiMjMxMmIxYjktOTQyMy00NzU1LTkyMzQtNzRiODU3OTUxMGFmIiwidCI6IjAzNmY4MTVjLTNkOTItNDJmMi1hNTk1LWQ2OWUxN2EwMzE5NCJ9",
        "financial": "https://app.powerbi.com/view?r=eyJrIjoiY2NjYzIyZGMtYjZjMi00NjA4LWE0MTMtZmNjY2E4NDM5MmQ4IiwidCI6IjAzNmY4MTVjLTNkOTItNDJmMi1hNTk1LWQ2OWUxN2EwMzE5NCJ9",
        "retail": "https://app.powerbi.com/view?r=eyJrIjoiNzE1YTM5OWMtYzAyNS00OGRlLThkNTYtZDFmZWIyZjRjOTBkIiwidCI6IjAzNmY4MTVjLTNkOTItNDJmMi1hNTk1LWQ2OWUxN2EwMzE5NCJ9",
        "hr": "https://app.powerbi.com/view?r=eyJrIjoiY2YwMTJlNzAtMTdmOC00ZGFmLTk5ZDgtNzAzMmE4N2ViMWJiIiwidCI6IjdiZTgzMDczLTJkY2ItNDg1OC05OTgwLTY4YjFiYjUzZGFmYyJ9",
        "crm": "https://app.powerbi.com/view?r=eyJrIjoiNTI5ZGQyYWEtOTkwMS00M2M5LWI4YzUtN2YwOGIzYmExMmVjIiwidCI6IjdiZTgzMDczLTJkY2ItNDg1OC05OTgwLTY4YjFiYjUzZGFmYyJ9"
    }
    report_url = report_links.get(report_type)
    if report_url:
        return render_template('dynamic_report.html', report_url=report_url, report_type=report_type)
    else:
        return "<h1>Report not found.</h1>", 404

# Flask app entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

