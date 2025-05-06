from flask import Flask, render_template
from backend.pos_tagger import mask_pos
# for text to speech not working yet
#from backend.tts_engine import save_audio
from backend.story_generator import generate_story
from flask import request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/temp')
def temp():
    return render_template("temp.html")

@app.route('/submit', methods=['POST'])
def submit():
    prompt = request.form.get("prompt", "")
    story = generate_story(prompt) if prompt else "No prompt provided."
    return render_template("index.html", story=story)

# edit once our generator is better
@app.route('/mask')
def mask_story():
    story = "The robot learned to dance with joy under the moonlight."
    masked = mask_pos(story, target_pos=["NOUN", "PROPN"])  # Mask nouns and names
    return render_template("mask.html", original=story, masked=masked)
# can't get working yet
#@app.route('/tts')
#def tts_demo():
#    story = "Once upon a time, a robot learned how to dance..."
#    audio_path = save_audio(story)
#    return render_template("tts_demo.html", audio_path=audio_path)

if __name__ == '__main__':
    app.run(debug=True)
