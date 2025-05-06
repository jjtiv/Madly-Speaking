from pos_tagger import get_pos_tags
import json

# Load story outputs from prompt_examples.json
with open('backend/prompt_examples.json', 'r', encoding='utf-8') as file:
    stories = json.load(file)

# Iterate over each story output and get POS tags
for i, story in enumerate(stories):
    input_text = story["output"]
    tags = get_pos_tags(input_text)

    print("______________________________________________________________________________")
    print(f"Story {i + 1}: {input_text}")
    print("POS Tags:")
    print(tags[:10])  # Show first 10 tagged words to keep output readable
