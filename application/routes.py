from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")
