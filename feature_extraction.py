# feature_extraction.py
import librosa
import numpy as np


def extract_features(file_path):
    """
    Extracts audio features from a given audio file.

    Parameters:
        file_path (str): Path to the audio file.

    Returns:
        dict: A dictionary containing extracted features.
    """
    try:
        # Load the audio file
        y, sr = librosa.load(file_path, duration=180)  # Load up to 3 minutes

        # Tempo (BPM)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        # Spectral Centroid (used as a proxy for "key" in this example)
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

        # Chroma Features (to determine the key)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)
        key_index = chroma_mean.argmax()
        key_dict = {
            0: 'C',
            1: 'C#',
            2: 'D',
            3: 'D#',
            4: 'E',
            5: 'F',
            6: 'F#',
            7: 'G',
            8: 'G#',
            9: 'A',
            10: 'A#',
            11: 'B'
        }
        key = key_dict.get(key_index, 'C')  # Default to 'C' if index not found

        # Genre (Placeholder: You can integrate a genre classification model here)
        genre = "Unknown"  # Implement genre classification as needed

        # Duration (in seconds)
        duration = librosa.get_duration(y=y, sr=sr)

        # Mood (Placeholder: You can integrate a mood classification model here)
        mood = "Neutral"  # Implement mood analysis as needed

        features = {
            'tempo': round(float(tempo), 2),
            'key': key,
            'genre': genre,
            'duration': round(duration, 2),
            'mood': mood
        }

        return features

    except Exception as e:
        print(f"Error extracting features: {e}")
        return {
            'tempo': None,
            'key': None,
            'genre': None,
            'duration': None,
            'mood': None
        }
