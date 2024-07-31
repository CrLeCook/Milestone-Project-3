from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize Flask app
app = Flask(__name__)

# Set a secret key for the app (for session security)
app.config["SECRET_KEY"] = "1791ed032aaf93226f79931c31c45e8d1402714a"

# Set MongoDB URI for connecting to the database
app.config['MONGO_URI'] = "mongodb+srv://admin:qvAysoXXgjAdSMlu@cluster0.09zb9yo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize PyMongo with the Flask app to interact with MongoDB
mongodb_client = PyMongo(app)

# Select the "flask_app" database from the MongoDB client
db = mongodb_client.cx["flask_app"]

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initialize LoginManager for user session management
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated
login_manager.login_message_category = 'info'  # Flash message category

# Import routes from the application package
from application import routes
