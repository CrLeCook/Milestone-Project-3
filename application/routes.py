from application import app
from flask import render_template
from .forms import TodoForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    return render_template("tech.html", title = "To Do | Habitual")

@app.route("/add_todo")
def add_todo():
    form = TodoForm()
    return render_template("add_todo.html", form = form)