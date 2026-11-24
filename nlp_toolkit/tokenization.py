
import nltk
from nltk.tokenize import word_tokenize


def tokenize_text(text: str) -> list[str]:
    """
    Split text into individual tokens.

    Args:
        text: Input text.

    Returns:
        A list of tokens.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    tokens = word_tokenize(text)

    return tokens
