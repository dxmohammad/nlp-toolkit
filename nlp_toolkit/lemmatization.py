from ._spacy import get_nlp


def lemmatize_text(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    doc = get_nlp()(text)

    return [
        token.lemma_
        for token in doc
        if not token.is_punct and not token.is_space
    ]