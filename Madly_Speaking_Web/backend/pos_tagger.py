import spacy

nlp = spacy.load("en_core_web_sm")

def get_pos_tags(text):
    # Generates part of speech for each word given a text
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags


# THis function might not be what we need as it might be redundant but I will leave it here for now. 
'''
def validate_input(user_inputs):
    # Validates that each word matches the pos it was tagged with. 
    
    validated = []
    for word, expected_pos in user_inputs:
        doc = nlp(word)
        word_pos = doc[0].pos_ if doc else None
        validated.append((word, expected_pos == word_pos))
    return validated
'''
