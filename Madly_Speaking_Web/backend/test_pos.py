from pos_tagger import get_pos_tags
import json
with open('prompt_examples.json', 'r') as file:
    stories = json.load(file)
#print(stories)
# Iterate over each story in the JSON file
for story in stories:
    input_text = story["output"]

    tags = get_pos_tags(input_text)

    print("______________________________________________________________________________")
    print(tags)