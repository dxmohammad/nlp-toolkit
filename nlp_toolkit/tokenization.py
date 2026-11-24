from nltk.tokenize import word_tokenize
from ._nltk import ensure_nltk_resource


def tokenize_text(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    ensure_nltk_resource("punkt_tab")

    return word_tokenize(text)