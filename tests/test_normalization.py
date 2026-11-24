
from nlp_toolkit.normalization import normalize_text

def test_lowercase():
    assert normalize_text("HELLO WORLD") == "hello world"


def test_extra_spaces():
    assert normalize_text("  Hello    NLP  ") == "hello nlp"


def test_unicode_normalization():
    assert normalize_text("ＡＢＣ") == "abc"


def test_empty_text():
    assert normalize_text("") == ""


def test_whitespace_only():
    assert normalize_text("     \n\t   ") == ""


def test_tabs_and_newlines():
    assert normalize_text("Hello\n\tNLP") == "hello nlp"


def test_idempotence():
    text = "  HELLO    ＮＬＰ  "

    first_result = normalize_text(text)
    second_result = normalize_text(first_result)

    assert first_result == second_result


def test_invalid_input():
    try:
        normalize_text(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_lowercase()
    test_extra_spaces()
    test_unicode_normalization()
    test_empty_text()
    test_whitespace_only()
    test_tabs_and_newlines()
    test_idempotence()
    test_invalid_input()

    print("All normalization tests passed!")
