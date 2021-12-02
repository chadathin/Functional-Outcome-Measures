from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
#import dbconfig

app = Flask(__name__,
            static_folder='assets',
            template_folder='templates')

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/score", methods=["POST", "GET"])
def score():
    if request.method == "POST":
        submission = request.form
        results = []
        for question in submission:
            results.append(int(submission[question]))
        print(results)
        return render_template("koos.html")
    else:
        return render_template("koos.html")

if __name__ == "__main__":
    app.run(debug=True)