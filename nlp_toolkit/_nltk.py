import nltk


_NLTK_RESOURCES = {
    "punkt_tab": "tokenizers/punkt_tab/english/",
    "stopwords": "corpora/stopwords",
    "averaged_perceptron_tagger_eng": (
        "taggers/averaged_perceptron_tagger_eng/"
    ),
}


def ensure_nltk_resource(resource: str) -> None:
    if resource not in _NLTK_RESOURCES:
        raise ValueError(f"Unknown NLTK resource: {resource}")

    try:
        nltk.data.find(_NLTK_RESOURCES[resource])
    except LookupError as error:
        raise LookupError(
            f"Required NLTK resource '{resource}' is missing. "
            f"Download it using: "
            f"python -c \"import nltk; nltk.download('{resource}')\""
        ) from error