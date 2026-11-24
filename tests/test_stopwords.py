
from nlp_toolkit.stopwords import remove_stopwords

def test_remove_stopwords():
    text = "I am learning the fundamentals of NLP"

    result = remove_stopwords(text)

    assert result == ["learning", "fundamentals", "NLP"]


def test_preserve_negation():
    text = "I do not like this product"

    result = remove_stopwords(text)

    assert "not" in result


def test_preserve_no():
    result = remove_stopwords("No, I cannot agree")

    assert "No" in result


def test_empty_text():
    assert remove_stopwords("") == []


def test_invalid_input():
    try:
        remove_stopwords(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


def test_invalid_language_type():
    try:
        remove_stopwords("Hello", language=123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


def test_unavailable_language():
    try:
        remove_stopwords("Hello", language="unknown_language")
    except LookupError:
        pass
    else:
        raise AssertionError("Expected LookupError")


if __name__ == "__main__":
    test_remove_stopwords()
    test_preserve_negation()
    test_preserve_no()
    test_empty_text()
    test_invalid_input()
    test_invalid_language_type()
    test_unavailable_language()

    print("All stopwords tests passed!")
