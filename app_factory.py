from flask import Flask
from models import db
from dotenv import load_dotenv
import os

# Function to create Flask app and set configurations
def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['ARTWORK_FOLDER'] = 'artworks'
    app.config['CELERY_BROKER_URL'] = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    
    db.init_app(app)
    
    # Ensure upload and artwork directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['ARTWORK_FOLDER'], exist_ok=True)
    
    return app
