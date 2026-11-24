from functools import lru_cache
import spacy


@lru_cache(maxsize=1)
def get_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except OSError as error:
        raise OSError(
            "spaCy English model is not installed. "
            "Install it using: "
            "python -m spacy download en_core_web_sm"
        ) from error