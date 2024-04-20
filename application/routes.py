from application import app
from flask import render_template, redirect, flash, request, url_for
from application import db
from .forms import TodoForm
from datetime import datetime
from bson import ObjectId

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/view_todos")
def get_todos():
    todos = []
    for todo in db.todos_flask.find().sort("date completed", -1):
        todo["_id"] = str(todo["_id"])
        todo["date completed"] = todo["date completed"].strftime("%b %d %Y %H:%M:%S")
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
        return redirect("/view_todos")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form = form)

@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash("Task successfully deleted", "success")
    return redirect("/view_todos")

@app.route("/update_todo/<id>", methods = ['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todos_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date completed": datetime.now()
        }})
        flash("Task successfully updated", "success")
        return redirect("/view_todos")
    else:
        form = TodoForm()

        todo = db.todos_flask.find_one_or_404({"_id": ObjectId(id)})
        print(todo)
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed", None)

    return render_template("add_todo.html", form = form)