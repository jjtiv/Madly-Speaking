from flask import Flask, render_template
from backend.pos_tagger import mask_pos
# for text to speech not working yet
# from backend.tts_engine import save_audio
from backend.story_generator import generate_story
from flask import request
import re

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
    if not prompt:
        return render_template("index.html", story="No prompt provided.")

    story = generate_story(prompt)
    masked_story = mask_pos(story, target_pos=["NOUN", "PROPN"])

    # Extract context-aware blanks for the form
    words = masked_story.split()
    placeholders = [w for w in words if w.startswith("__") and w.endswith("__")]

    context_blanks = []
    used = set()
    counter = 0
    for i, word in enumerate(words):
        if word in placeholders and word not in used:
            used.add(word)
            prev_word = words[i - 1] if i > 0 else ""
            next_word = words[i + 1] if i < len(words) - 1 else ""
            context = f"... {prev_word} {word} {next_word} ..."
            context_blanks.append((word, counter, context))
            counter += 1

    return render_template("fill_in.html", masked_story=masked_story, context_blanks=context_blanks)
# edit once our generator is better
@app.route('/mask')
def mask_story():
    story = "The robot learned to dance with joy under the moonlight."
    masked_story = mask_pos(story, target_pos=["NOUN", "PROPN"], max_masks=3)
    return render_template("mask.html", original=story, masked=masked_story)


@app.route('/final_story', methods=['POST'])
def final_story():
    masked_story = request.form.get("masked_story", "")

    # find all placeholders like __NOUN__, __PROPN__, etc.
    placeholders = re.findall(r'__\w+__', masked_story)

    # collect user inputs
    replacements = []
    for i in range(len(placeholders)):
        value = request.form.get(f"fill{i}", "")
        replacements.append(value)

    # replace each placeholder one by one
    for i, placeholder in enumerate(placeholders):
        masked_story = masked_story.replace(placeholder, replacements[i], 1)

    return render_template("final_story.html", story=masked_story)


if __name__ == '__main__':
    app.run(debug=True)
