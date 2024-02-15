from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Setup of key Flask object (app)
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Setup SQLAlchemy object and properties for the database (db)
dbURI = 'sqlite:///volumes/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
Migrate(app, db)

# Images storage
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # maximum size of uploaded content
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']  # supported file types
app.config['UPLOAD_FOLDER'] = 'volumes/uploads/'  # location of user uploaded content
