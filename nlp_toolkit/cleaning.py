
import re


def clean_text(
    text: str,
    remove_punctuation: bool = True,
    remove_numbers: bool = False,
    remove_extra_spaces: bool = True
) -> str:
    """
    Clean text by optionally removing punctuation and numbers,
    and normalizing whitespace.

    Args:
        text: Input text.
        remove_punctuation: Replace punctuation with spaces.
        remove_numbers: Remove numeric characters.
        remove_extra_spaces: Collapse repeated whitespace.

    Returns:
        Cleaned text.

    Raises:
        TypeError: If text or any option has an invalid type.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    options = {
        "remove_punctuation": remove_punctuation,
        "remove_numbers": remove_numbers,
        "remove_extra_spaces": remove_extra_spaces
    }

    for name, value in options.items():
        if not isinstance(value, bool):
            raise TypeError(f"{name} must be a boolean.")

    if remove_punctuation:
        text = re.sub(r"[^\w\s]|_", " ", text)

    if remove_numbers:
        text = re.sub(r"\d+", "", text)

    if remove_extra_spaces:
        text = re.sub(r"\s+", " ", text).strip()

    return text
