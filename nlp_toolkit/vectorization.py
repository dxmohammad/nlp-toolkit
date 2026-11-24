
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer
)


def _validate_documents(documents: list[str]) -> None:
    """Validate input documents."""

    if not isinstance(documents, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(doc, str) for doc in documents):
        raise TypeError("All documents must be strings.")

    if not documents or not any(doc.strip() for doc in documents):
        raise ValueError("Documents cannot be empty.")


def _vectorize_documents(
    documents: list[str],
    vectorizer: CountVectorizer | TfidfVectorizer
) -> tuple[csr_matrix, list[str]]:
    """Convert documents into numerical vectors."""

    _validate_documents(documents)

    try:
        matrix = vectorizer.fit_transform(documents)
    except ValueError as error:
        raise ValueError(
            "No valid vocabulary found in the documents."
        ) from error

    vocabulary = vectorizer.get_feature_names_out().tolist()

    return matrix, vocabulary


def bag_of_words(
    documents: list[str]
) -> tuple[csr_matrix, list[str]]:
    """
    Convert text documents into Bag of Words vectors.
    """

    vectorizer = CountVectorizer()

    return _vectorize_documents(documents, vectorizer)


def tfidf_vectorization(
    documents: list[str]
) -> tuple[csr_matrix, list[str]]:
    """
    Convert text documents into TF-IDF vectors.
    """

    vectorizer = TfidfVectorizer()

    return _vectorize_documents(documents, vectorizer)
