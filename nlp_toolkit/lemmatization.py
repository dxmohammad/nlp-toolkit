
import spacy

nlp = spacy.load("en_core_web_sm")


def lemmatize_text(text: str) -> list[str]:
    """
    Convert words in a text into their base forms
    using spaCy's English language model.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    doc = nlp(text)

    lemmas = [
        token.lemma_
        for token in doc
        if not token.is_punct and not token.is_space
    ]

    return lemmas
