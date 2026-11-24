
from nlp_toolkit.lemmatization import lemmatize_text

def test_lemmatization():
    text = "The mice were running and the students were studying"

    result = lemmatize_text(text)

    assert "mouse" in result
    assert "be" in result
    assert "run" in result
    assert "study" in result


def test_empty_text():
    assert lemmatize_text("") == []


def test_invalid_input():
    try:
        lemmatize_text(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_lemmatization()
    test_empty_text()
    test_invalid_input()

    print("All lemmatization tests passed!")
