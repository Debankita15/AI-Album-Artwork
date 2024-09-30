# AI-Album-Artwork

# AI Album Artwork Generator

### **Project Overview**
This project is an AI-powered tool designed to generate custom album artwork based on the features of uploaded audio files. It leverages audio feature extraction (tempo, key, genre, etc.) and stable diffusion models to create unique album covers that visually represent the mood and style of the music.

### **Work in Progress**
This project is part of an ongoing volunteer effort. The work is still in progress, with various updates made each week. The current features include:

- **Audio Feature Extraction:** Extract key characteristics of audio files using `librosa`.
- **AI-Powered Artwork Generation:** Generate artwork based on extracted features using `Stable Diffusion`.
- **Background Processing with Celery:** Tasks like feature extraction and artwork generation are processed in the background using `Celery` and `Redis`.

### **Key Features**
- Upload audio files in `.mp3` format.
- Automatically extract features such as tempo, key, genre, and mood.
- Generate album artwork using a Stable Diffusion model based on the extracted features.
- Display generated artwork on a web-based dashboard built using Flask.
- Support for background task processing with `Celery` and `Redis`.

---

### **Installation**

1. **Clone the repository**:
       ```bash
       git clone https://github.com/your_username/ai_album_artwork.git
       cd ai_album_artwork

2. **Install the required dependencies**:
      ```bash
      pip install -r requirements.txt

3. **Configure environment variables**:
  Create a .env file and add the following variables:

    ```bash
    FLASK_SECRET_KEY=<your_flask_secret_key>
    CELERY_BROKER_URL=redis://localhost:6379/0
    CELERY_RESULT_BACKEND=redis://localhost:6379/0
    HUGGINGFACE_TOKEN=<your_huggingface_token>
    
4. **Start Redis using Docker**:
  Make sure you have Docker installed. Then, run the following command to start Redis:

    ```bash
    docker run -d -p 6379:6379 --name redis-server redis
    Run Celery Worker:
    
    ```bash
    celery -A celery_worker.celery worker --loglevel=info --pool=solo

5. **Start the Flask app**:

    ```python
    python app.py

6. **Visit the application**:
  Open your browser and navigate to [http://127.0.0.1:5000].

---

### **Usage**
- Upload an `.mp3` file.
- The app extracts audio features (tempo, key, genre, etc.).
- Album artwork is generated in the background using AI based on the extracted features.
- The dashboard displays the generated album artwork, allowing you to download it.

---

### **Volunteer Work & Progress**
This project is being developed as part of a volunteer effort. Below is a weekly log of the development progress.

---

### **Weekly Update Log**

#### **Week 1 (August 19 - August 25, 2024):**
- Initial project setup with Flask and Celery.
- Integrated `librosa` for audio feature extraction.
- Set up basic file upload functionality and SQLite database for storing track metadata.

#### **Week 2 (August 26 - September 1, 2024):**
- Implemented Stable Diffusion for generating album artwork based on audio features.
- Added support for background processing with Celery and Redis.
- Worked on setting up environment variables and authentication with Hugging Face API.

#### **Week 3 (September 2 - September 8, 2024):**
- Improved the Flask UI with Bootstrap.
- Added a basic dashboard to display uploaded tracks and generated artwork.
- Started exploring how to include song lyrics in the generation process.

#### **Week 4 (September 9 - September 15, 2024):**
- Fixed bugs related to task processing and Celery worker issues.
- Implemented a fallback system for artwork generation failures.
- Continued refining the audio feature extraction process.

#### **Week 5 (September 16 - September 22, 2024):**
- Improved the artwork generation by integrating more mood and genre-related prompts.
- Worked on displaying artwork directly within the web application dashboard.
- Refined the workflow to ensure smooth Celery task execution.

#### **Week 6 (September 23 - September 27, 2024):**
- Fixed errors related to circular imports in Celery.
- Added support for lyrics-based artwork generation (still in progress).
- Tested the app end-to-end with sample tracks and artwork generation.

---

### **To-Do List**
- [ ] Fully integrate lyrics into the artwork generation process.
- [ ] Add more customization options for users when generating artwork.
- [ ] Improve error handling and add more unit tests.
- [ ] Deploy the app to a cloud environment (e.g., AWS, Heroku).

---

### **License**
This project is licensed under the MIT License.
