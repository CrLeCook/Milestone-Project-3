from flask import Flask
from flask_pymongo import PyMongo

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

# Import routes from the application package
from application import routes
