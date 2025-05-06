import spacy

nlp = spacy.load("en_core_web_sm")

def get_pos_tags(text):
    """
    Returns a list of (word, POS_tag) tuples for a given text.
    """
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

# Used for testing
#def validate_input(user_inputs):
 #   """
 #   Validates whether user-supplied words match expected POS tags.
 #   user_inputs: List of (word, expected_pos) pairs
 #   Returns: List of (word, is_valid) pairs
 #   """
  #  validated = []
  #  for word, expected_pos in user_inputs:
  #     doc = nlp(word)
  #      actual_pos = doc[0].pos_
  #      is_valid = actual_pos == expected_pos
  #      validated.append((word, is_valid))
  #  return validated

def mask_pos(text, target_pos=["NOUN"]):
    """
    Replaces words matching target POS tags with blanks (____).
    """
    doc = nlp(text)
    masked_tokens = ["____" if token.pos_ in target_pos else token.text for token in doc]
    return " ".join(masked_tokens)
