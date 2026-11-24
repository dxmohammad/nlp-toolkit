
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str) -> list[dict[str, str]]:
    """
    Extract named entities from text using spaCy.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    doc = nlp(text)

    entities = [
        {
            "text": entity.text,
            "label": entity.label_,
            "description": spacy.explain(entity.label_)
        }
        for entity in doc.ents
    ]

    return entities
