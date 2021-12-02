from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
# import db_config

app = Flask(__name__,
            static_folder='assets',
            template_folder='templates')
app.secret_key = "tis_but_a_key"

@app.route("/")
def home():
    return render_template("base.html")

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
        return render_template("results_page.html", result=result, assessment=assessment)
    else:
        return "No assessment performed!"

@app.route("/koos", methods=["POST", "GET"])
def koos():
    session['assessment'] = "koos"
    return render_template("koos.html")


if __name__ == "__main__":
    app.run(debug=True)
