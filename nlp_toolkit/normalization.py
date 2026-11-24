
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize text using Unicode normalization,
    lowercase conversion, and whitespace cleanup.

    Args:
        text: Input text.

    Returns:
        Normalized text.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Apply Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Convert text to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = " ".join(text.split())

    return text
