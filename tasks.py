from celery_worker import celery
from models import db, Track, Artwork
from feature_extraction import extract_features
from ai_artwork_generation import generate_artwork
import os

@celery.task(name="tasks.generate_artwork_task")
def generate_artwork_task(track_id, file_path):
    """
    Celery task to generate artwork based on audio features.
    """

    from app_factory import create_app
    app = create_app()
    
    with app.app_context():
        try:
            # Task logic here...
            features = extract_features(file_path)
            tempo = features.get('tempo')
            key = features.get('key')
            genre = features.get('genre')
            duration = features.get('duration')
            mood = features.get('mood')

            # Retrieve the track from the database
            track = Track.query.get(track_id)
            if not track:
                print(f"Track with ID {track_id} not found.")
                return

            # Update track with extracted features
            track.tempo = round(tempo, 2) if tempo else None
            track.key = key
            track.genre = genre
            track.duration = round(duration, 2) if duration else None
            track.mood = mood
            db.session.commit()

            # Create prompt for AI model
            prompt = f"Create an album cover with a {mood} mood, tempo {tempo} BPM, key {key}, genre {genre}."

            # Define output path
            artwork_filename = f"artwork_{track_id}.png"
            artwork_path = os.path.join('artworks', artwork_filename)

            # Generate artwork
            generate_artwork(prompt, artwork_path)

            # Update track with artwork path
            track.artwork_path = artwork_path
            db.session.commit()

            print(f"Artwork for Track ID {track_id} generated successfully.")

        except Exception as e:
            print(f"Error processing Track ID {track_id}: {e}")
            track = Track.query.get(track_id)
            if track:
                track.artwork_path = "error"
                db.session.commit()

