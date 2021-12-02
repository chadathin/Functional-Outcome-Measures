from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
# import db_config

app = Flask(__name__,
            static_folder='assets',
            template_folder='templates')
app.secret_key = "tis_but_a_key"

avail_assessments = {
    "KOOS JR": '/koos',
    "ODI": "/odi"
}

@app.route("/")
def home():
    return render_template("base.html", header="How it works", available=avail_assessments)

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        # Get all form radio values
        submission = request.form

        # Get the incoming assessment name
        assessment = session['assessment']

        # Sanitizes selected form values
        results = []

        for question in submission:
            results.append(int(submission[question]))

        result = sum(results)

        print(avail_assessments)
        return render_template("results_page.html", result=result, assessment=assessment, header="Results", available=avail_assessments)
    else:
        return "No assessment performed!"

@app.route("/koos", methods=["POST", "GET"])
def koos():
    session['assessment'] = "KOOS JR"
    return render_template("koos.html", header = "KOOS JR", available=avail_assessments)


if __name__ == "__main__":
    app.run(debug=True)
