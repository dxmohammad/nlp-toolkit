from nltk.tokenize import sent_tokenize
from ._nltk import ensure_nltk_resource


def tokenize_sentences(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not text.strip():
        return []

    ensure_nltk_resource("punkt_tab")

    return sent_tokenize(text)