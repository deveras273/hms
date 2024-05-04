import os
from flask import Flask, render_template, request, redirect, url_for
import pyodbc
# from models import authenticate

app = Flask(__name__)

# # Get SQL Server connection string from environment variable
# connection_string = os.environ.get('SQL_CONNECTION_STRING')

# if connection_string is None:
#     raise ValueError("SQL_CONNECTION_STRING environment variable is not set")

# # Connect to SQL Server database
# cnxn = pyodbc.connect(connection_string)

# Connect to your SQL Server database
server = 'LAPTOP-I86HA789'
database = 'WebApplication'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')


# server_uri = "ldap://127.0.0.1"
# domain = "domain.com"

# @app.route("/", methods=['POST', 'GET'])
# def login():
#     context = {}
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         try:
#             authenticate(server_uri, domain, username, password)
#             return redirect("/loggedin")
#         except ValueError as err:
#             context["error"] = err.message

#     return render_template("login.html", **context)


# @app.route("/loggedin")
# def loggedin():
#     return "Successfully logged in!"


@app.route('/')
def index():
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    return render_template('index.html', patients=patients)

@app.route('/details/<int:patient_id>')
def patient_details(patient_id):
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    patient = cursor.fetchone()
    if patient:
        return render_template('details.html', patient=patient)
    else:
        return "Patient not found"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
