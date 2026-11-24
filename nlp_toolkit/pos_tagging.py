from nltk import pos_tag
from nltk.tokenize import word_tokenize
from ._nltk import ensure_nltk_resource


def get_pos_tags(text: str) -> list[tuple[str, str]]:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    ensure_nltk_resource("punkt_tab")
    ensure_nltk_resource("averaged_perceptron_tagger_eng")

    tokens = word_tokenize(text)

    return pos_tag(tokens)