
from nlp_toolkit.vectorization import bag_of_words, tfidf_vectorization

documents = [
    "I love AI",
    "I love Python",
    "AI is powerful"
]


def test_bag_of_words():
    matrix, vocabulary = bag_of_words(documents)

    assert matrix.shape[0] == 3
    assert matrix.shape[1] == len(vocabulary)
    assert "love" in vocabulary
    assert "python" in vocabulary


def test_tfidf():
    matrix, vocabulary = tfidf_vectorization(documents)

    assert matrix.shape[0] == 3
    assert matrix.shape[1] == len(vocabulary)
    assert "love" in vocabulary
    assert "python" in vocabulary


def test_empty_documents():
    for function in [bag_of_words, tfidf_vectorization]:
        try:
            function([])
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")


def test_empty_vocabulary():
    documents = ["I", "a", "!"]

    for function in [bag_of_words, tfidf_vectorization]:
        try:
            function(documents)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")


def test_invalid_input():
    for function in [bag_of_words, tfidf_vectorization]:
        try:
            function("I love AI")
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")


def test_invalid_document():
    for function in [bag_of_words, tfidf_vectorization]:
        try:
            function(["I love AI", 123])
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_bag_of_words()
    test_tfidf()
    test_empty_documents()
    test_empty_vocabulary()
    test_invalid_input()
    test_invalid_document()

    print("All vectorization tests passed!")
