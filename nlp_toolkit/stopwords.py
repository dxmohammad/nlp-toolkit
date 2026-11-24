from ._nltk import ensure_nltk_resource
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_stopwords(
    text: str,
    language: str = "english"
) -> list[str]:
    """
    Remove common stopwords from text while preserving negation.

    Args:
        text: Input text.
        language: Stopwords language.

    Returns:
        A list of filtered tokens.

    Raises:
        TypeError: If input types are invalid.
        LookupError: If required NLTK resources are unavailable.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not isinstance(language, str):
        raise TypeError("Language must be a string.")

    ensure_nltk_resource("stopwords")
    ensure_nltk_resource("punkt_tab")

    try:
        stop_words = set(stopwords.words(language))
    except (LookupError, OSError) as error:
        raise LookupError(
            f"Stopwords data for '{language}' is unavailable."
        ) from error

    # Preserve negation words
    stop_words.discard("not")
    stop_words.discard("no")

    tokens = word_tokenize(text)

    filtered_tokens = [
        word for word in tokens
        if word.lower() not in stop_words
    ]

    return filtered_tokens