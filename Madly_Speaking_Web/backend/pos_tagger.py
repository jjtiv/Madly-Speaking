import spacy
import random

nlp = spacy.load("en_core_web_sm")

def get_pos_tags(text):
    """
    Returns a list of (word, POS_tag) tuples for a given text.
    """
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

# Loads the english model from spacy for POS tagging
nlp = spacy.load("en_core_web_sm")

# Replaces up to max_masks words in the input text 
def mask_pos(text, target_pos=["NOUN", "PROPN"], max_masks=3):
    # parse the text using spacy pipeline
    doc = nlp(text)
    # list of common words to avoid masking even if they match POS
    stop_words = {"time", "money", "day", "first", "one", "thing", "it"}
    # holds the final list of words for the ouput
    masked_tokens = []
    count = 0
    for i, token in enumerate(doc):
        # get the previous word or empty string if its the first word
        prev = doc[i - 1].text.lower() if i > 0 else ""
        # check the masking criteria
        if (
            token.pos_ in target_pos
            and token.text.lower() not in stop_words
            and prev not in {"the", "a", "an"}  # prevents masking after "to the"
            and count < max_masks
        ):
            # replace word with a placeholder indicating its POS
            masked_tokens.append(f"__{token.pos_}__")
            count += 1
        else:
            # keep the original word
            masked_tokens.append(token.text)
    # join all tokens back into a string.
    return " ".join(masked_tokens)


