import string
import re

def strip_punctuation(text: str, excepted=""):
    punctuation = string.punctuation
    for c in excepted:
        punctuation = punctuation.replace(c, "")
    text = text.translate(str.maketrans('', '', punctuation))
    text = re.sub(r"\s{2,}", " ", text)
    return text