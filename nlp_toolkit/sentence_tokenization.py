
from nltk.tokenize import sent_tokenize


def tokenize_sentences(text: str) -> list[str]:
    """
    Split text into individual sentences using NLTK.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not text.strip():
        return []

    sentences = sent_tokenize(text)

    return sentences
