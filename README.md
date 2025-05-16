# If you have any problems during this set up please email ebeyers1@umbc.edu

# Madly Speaking Web

Madly Speaking Web is an interactive web application that generates context aware stories based on user prompts, allows users to fill in blanks for a Mad Libs-style experience, and supports real-time text-to-speech synthesis.

## Features

- **Story Generation**: Uses a fine-tuned T5 model to generate creative short stories from prompts.
-  **Part-of-Speech Masking**: Masks nouns and proper nouns to create interactive fill-in-the-blank stories.
-  **Context-Aware Blanks**: Displays blanks with surrounding context to help users make fun and fitting choices.
-  **Text-to-Speech (TTS)**: Reads generated stories aloud using gTTS, playable directly in the browser. 
-  **Flask Web Interface**: Lightweight Python backend with a user-friendly HTML frontend.

## How to Run

1. Clone the repo:
```bash
git clone git@github.com:jjtiv/Madly-Speaking.git
cd Madly-Speaking/Madly_Speaking_Web
```
2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate

3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Run the web app:
```bash
python app.py
```

5. Navigate to  Running on `http://127.0.0.1:5000` in your browser.

## Project Structure

```
Madly_Speaking_Web/
├── app.py                    # Flask backend
├── templates/                # HTML templates
│   ├── index.html
│   ├── fill_in.html
│   ├── final_story.html
│   ├── mask.html
│   ├── temp.html
├── backend/
│   ├── pos_tagger.py         # POS masking logic
│   ├── story_generator.py    # T5 model story generation
│   ├── tts_engine.py         # TTS using gTTS
├── static/                   # CSS, Images, Fonts
└── README.md                 
```

## Technologies

- Flask (Python)
- Hugging Face Transformers T5
- gTTS (Google Text-to-Speech)
- HTML/CSS, React
- Spacy (POS Tagger)


## Future Improvements

- Add more tones (e.g., dramatic, mysterious, romantic)
- Improve coherence in masking logic



