from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from .forms import TodoForm, RegistrationForm, LoginForm
from datetime import datetime
from bson import ObjectId
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = str(user_id)
        self.username = username
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            return User(str(user['_id']), user['username'], user['password'])
        return None

    @staticmethod
    def get_by_username(username):
        user = db.users.find_one({"username": username})
        if user:
            return User(str(user['_id']), user['username'], user['password'])
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/view_todos")
@login_required
def get_todos():
    todos = []
    for todo in db.todos_flask.find().sort("date completed", -1):
        todo["_id"] = str(todo["_id"])
        todo["date completed"] = todo["date completed"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("view_todos.html", todos=todos)

@app.route("/add_todo", methods=["POST", "GET"])
@login_required
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
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
        return redirect(url_for('get_todos'))
    return render_template("add_todo.html", form=form)

@app.route("/delete_todo/<id>")
@login_required
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash("Task successfully deleted", "success")
    return redirect(url_for('get_todos'))

@app.route("/update_todo/<id>", methods=['POST', 'GET'])
@login_required
def update_todo(id):
    form = TodoForm()
    if form.validate_on_submit():
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
        return redirect(url_for('get_todos'))
    todo = db.todos_flask.find_one_or_404({"_id": ObjectId(id)})
    form.name.data = todo.get("name", None)
    form.description.data = todo.get("description", None)
    form.completed.data = todo.get("completed", None)
    return render_template("add_todo.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.users.insert_one({
            'username': form.username.data,
            'password': hashed_password
        })
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
