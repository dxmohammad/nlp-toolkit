
from nltk import pos_tag
from nltk.tokenize import word_tokenize


def get_pos_tags(text: str) -> list[tuple[str, str]]:
    """
    Identify the grammatical category of each word
    using NLTK POS Tagging.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    tokens = word_tokenize(text)

    tagged_words = pos_tag(tokens)

    return tagged_words
