from flask import render_template, request, redirect, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
from models import db, Track, Artwork
from app_factory import create_app
import os

# Initialize Flask app using factory function
app = create_app()

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Create Track entry
        new_track = Track(filename=filename)
        db.session.add(new_track)
        db.session.commit()

        # Trigger background task for processing (import the task here)
        from tasks import generate_artwork_task
        generate_artwork_task(new_track.id, file_path)

        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    tracks = Track.query.all()
    return render_template('dashboard.html', tracks=tracks)

@app.route('/artwork/<int:track_id>')
def artwork(track_id):
    artwork = Artwork.query.filter_by(track_id=track_id).first()
    if artwork:
        return send_file(artwork.image_path, as_attachment=True)
    else:
        return "Artwork is being generated. Please check back later."
    
# Serve artwork images
@app.route('/artworks/<filename>')
def serve_artwork(filename):
    return send_from_directory(app.config['ARTWORK_FOLDER'], filename)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
