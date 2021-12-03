from flask import Flask, render_template, request, session, redirect, url_for
import sys
from flask_mysqldb import MySQL

# ========== My Modules ====================

from funcs import randString
from koos import koos_lookup
import mariadb
# import db_config

app = Flask(__name__, static_folder='static', template_folder='templates')

# app.config['MYSQL_HOST'] = '127.0.0.1:3307'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'foms'
#
# mysql = MySQL(app)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Nicole0406!",
        host="127.0.0.1",
        port=3307,
        database="foms"
    )
    print("Database connected!")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

conn.autocommit = False

# Get Cursor
cur = conn.cursor()

assessmentID = randString()

app.secret_key = assessmentID

def insertSomething(cursor):
    # cur = conn.cursor()

    cursor.execute("INSERT INTO assessments (unique_ident, name, score) VALUES (?, ?, ?);",
                ("ABCDF", "QuickDash", 55))
    print("sent!")
    conn.commit()
                                                        # ============= NOTE TO SELF =============
    conn.close()                                        # RELOADER IS CAUSING TWO EXECUTES TO BE SENT
    return 0                                            # CAN STOP BY TURNING OFF DEBUG, OR MOVING THIS FUNCTION TO NOT BE GLOBAL

insertSomething(cur)

avail_assessments = {
    "KOOS JR": '/koos',
    "ODI": "/odi"
}

@app.route("/")
def home():
    return render_template("base.html", header="How it works", available=avail_assessments)

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "GET":
        return render_template("results_page.html", result="No Score To Save! (Please perform an assessment.)", available=avail_assessments)
    elif request.method == "POST":
        result = session['result']
        assessment = session['assessment']
        return render_template("results_page.html", result=result, assessment=assessment, header="Results", available=avail_assessments, ident=assessmentID)

@app.route("/store_result")
def store_result():
    pass

@app.route("/koos", methods=["POST", "GET"])
def koos():
    session['assessment'] = "KOOS JR"
    if request.method == "POST":
        # Get all form radio values
        submission = request.form

        # Sanitizes selected form values
        results = []
        for question in submission:
            results.append(int(submission[question]))

        # Sum the selected values and find score from lookup table
        koos_result = sum(results)
        koos_result = koos_lookup[result]

        # Update session['result']
        session['result'] = koos_result
        return redirect(url_for("result"), code=307) # <- code needs to be 307 to maintain "POST" request

    return render_template("koos.html", header="KOOS JR", available=avail_assessments)


if __name__ == "__main__":
    app.run(debug=True)
