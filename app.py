from flask import Flask, render_template, request, session, redirect, url_for

from flask_mysqldb import MySQL

# ========== My Modules ====================

from funcs import randString
from koos import koos_lookup
# import db_config

app = Flask(__name__, static_folder='static', template_folder='templates')

assessmentID = randString()

app.secret_key = assessmentID


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
