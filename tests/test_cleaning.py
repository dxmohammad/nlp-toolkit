
from nlp_toolkit.cleaning import clean_text


def test_remove_punctuation():
    assert clean_text("Hello!!! NLP.") == "Hello NLP"


def test_punctuation_separation():
    assert clean_text("state-of-the-art") == "state of the art"


def test_underscore_removal():
    assert clean_text("Hello_World") == "Hello World"


def test_remove_numbers():
    assert clean_text(
        "Learning NLP 123",
        remove_numbers=True
    ) == "Learning NLP"


def test_remove_extra_spaces():
    assert clean_text("Hello     NLP") == "Hello NLP"


def test_preserve_extra_spaces():
    result = clean_text(
        "Hello     NLP",
        remove_extra_spaces=False
    )
    assert result == "Hello     NLP"


def test_invalid_input():
    try:
        clean_text(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


def test_invalid_options():
    for option in [
        {"remove_punctuation": "yes"},
        {"remove_numbers": 1},
        {"remove_extra_spaces": None}
    ]:
        try:
            clean_text("Hello NLP", **option)
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_remove_punctuation()
    test_punctuation_separation()
    test_underscore_removal()
    test_remove_numbers()
    test_remove_extra_spaces()
    test_preserve_extra_spaces()
    test_invalid_input()
    test_invalid_options()

    print("All cleaning tests passed!")
