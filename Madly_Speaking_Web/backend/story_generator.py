from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
print("Model loading... please wait.")
# load T5 model + tokenizer once globally
tokenizer = T5Tokenizer.from_pretrained("jakinmo1/csv_final")
model = T5ForConditionalGeneration.from_pretrained("jakinmo1/csv_final")

def generate_story(prompt, max_length=150, num_beams=4):

    input_text = f"Write a story about {prompt}"

    print(f"DEBUG: Input to model -> {input_text}")

    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=num_beams,
        early_stopping=True,
        no_repeat_ngram_size=2
    )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
