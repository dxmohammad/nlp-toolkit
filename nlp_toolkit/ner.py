import spacy
from ._spacy import get_nlp


def extract_entities(text: str) -> list[dict[str, str]]:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    doc = get_nlp()(text)

    return [
        {
            "text": entity.text,
            "label": entity.label_,
            "description": spacy.explain(entity.label_)
        }
        for entity in doc.ents
    ]