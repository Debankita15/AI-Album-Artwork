from celery import Celery
from app_factory import create_app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def make_celery(app=None):
    app = app or create_app()
    
    celery = Celery(
        app.import_name,
        broker=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
        backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    )
    
    celery.conf.update(app.config)
    
    return celery

app = create_app()  # Create Flask app here
celery = make_celery(app)

# Explicitly import and register the task here
# from tasks import generate_artwork_task  # Ensure the task is imported
# celery.tasks.register(generate_artwork_task)