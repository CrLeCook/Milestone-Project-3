from application import app
from flask import render_template, redirect, flash, request, url_for
from application import db
from .forms import TodoForm
from datetime import datetime
from bson import ObjectId

# Route for the index page
@app.route("/")
def index():
    return render_template("index.html")

# Route for the tech page
@app.route("/tech")
def tech():
    return render_template("tech.html")

# Route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for viewing all todos
@app.route("/view_todos")
def get_todos():
    todos = []
    # Retrieve todos from the database and format their date
    for todo in db.todos_flask.find().sort("date completed", -1):
        todo["_id"] = str(todo["_id"])
        todo["date completed"] = todo["date completed"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)

    return render_template("view_todos.html", todos=todos)

# Route for adding a new todo
@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        # Insert the new todo into the database
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
    return render_template("add_todo.html", form=form)

# Route for deleting a todo
@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash("Task successfully deleted", "success")
    return redirect("/view_todos")

# Route for updating a todo
@app.route("/update_todo/<id>", methods=['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        # Update the todo in the database
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

        # Populate form fields with existing todo data
        todo = db.todos_flask.find_one_or_404({"_id": ObjectId(id)})
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed", None)

    return render_template("add_todo.html", form=form)
