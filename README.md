Flask Report Viewer Application
Overview
This Flask-based web application provides a platform to view dynamic and static reports, leveraging Power BI for visualizations. 
The application is live at http://sangamsoftsol.com/, hosted on AWS with domain management via Route53.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)







