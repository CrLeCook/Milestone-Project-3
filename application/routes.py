from application import app
from flask import render_template, redirect, flash, request, url_for
from application import db
from .forms import TodoForm
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    return render_template("tech.html", title = "To Do | Habitual")
def get_todos():
    todos = []
    for todo in db.todos_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)

    return render_template("view_todos.html", todos = todos)

@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todos_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date completed": datetime.now()
        })
        flash("Task successfully created", "success")
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form = form)