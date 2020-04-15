from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

Uploads = "./app/static/profilepics"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gztpvcswgnpipg:63c75dbb9f460474fbbe9c471a36bfbf6c71187b120a202258f68beb7e9bf4b3@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d9e3ql54457peh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['Uploads'] = Uploads

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
