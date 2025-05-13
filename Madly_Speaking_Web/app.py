from flask import Flask, render_template, request, send_file
from backend.pos_tagger import mask_pos
# for text to speech not working yet
#from backend.tts_engine import save_audio
from backend.story_generator import generate_story
from flask import request
from backend.tts_engine import save_audio

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

@app.route('/tts')
def tts():
    # read `text` from querystring
    text = request.args.get('text', '').strip()
    if not text:
        return "Error: no text provided", 400

    # generate MP3 in memory
    mp3_fp = save_audio(text)

    # stream it back
    return send_file(
        mp3_fp,
        mimetype='audio/mpeg',
        as_attachment=False,
        download_name='speech.mp3'
    )

if __name__ == '__main__':
    app.run(debug=True)
