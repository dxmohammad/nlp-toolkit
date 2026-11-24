
from nltk.stem import PorterStemmer


_stemmer = PorterStemmer()


def stem_words(words: list[str]) -> list[str]:
    """
    Apply Porter Stemming to a list of English words.

    Args:
        words: A list of input words.

    Returns:
        A list of stemmed words.

    Raises:
        TypeError: If input is not a list of strings.
    """

    if not isinstance(words, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(word, str) for word in words):
        raise TypeError("All items must be strings.")

    stemmed_words = [
        _stemmer.stem(word)
        for word in words
    ]

    return stemmed_words
