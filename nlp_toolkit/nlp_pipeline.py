
from .cleaning import clean_text
from .normalization import normalize_text
from .tokenization import tokenize_text
from .stopwords import remove_stopwords
from .stemming import stem_words
from .lemmatization import lemmatize_text
from .pos_tagging import get_pos_tags
from .ner import extract_entities
from .sentence_tokenization import tokenize_sentences

def process_text(text: str) -> dict:
    """
    Process text using the NLP Toolkit modules.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not text.strip():
        raise ValueError("Input text cannot be empty.")

    # Text preprocessing
    cleaned_text = clean_text(text)

    normalized_text = normalize_text(cleaned_text)

    # Token processing
    tokens = tokenize_text(normalized_text)

    filtered_tokens = remove_stopwords(normalized_text)

    stemmed_tokens = stem_words(filtered_tokens)

    # Linguistic analysis on original text
    sentences = tokenize_sentences(text)

    lemmas = lemmatize_text(text)

    pos_tags = get_pos_tags(text)

    entities = extract_entities(text)

    return {
        "cleaned_text": cleaned_text,
        "normalized_text": normalized_text,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "stemmed_tokens": stemmed_tokens,
        "sentences": sentences,
        "lemmas": lemmas,
        "pos_tags": pos_tags,
        "entities": entities
    }
