from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
print("Model loading... please wait.")
# load T5 model + tokenizer once globally
tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-base")
model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-base")

def generate_story(prompt, max_length=150, num_beams=4):

    input_text = f"Write a short creative story about the following: {prompt}"

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
