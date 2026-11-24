
from nlp_toolkit.stemming import stem_words

def test_stemming():
    words = ["playing", "played", "plays", "studies"]

    result = stem_words(words)

    assert result == ["play", "play", "play", "studi"]


def test_empty_list():
    assert stem_words([]) == []


def test_invalid_input():
    try:
        stem_words("playing")
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


def test_invalid_list_items():
    try:
        stem_words(["playing", 123, "studies"])
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_stemming()
    test_empty_list()
    test_invalid_input()
    test_invalid_list_items()

    print("All stemming tests passed!")
