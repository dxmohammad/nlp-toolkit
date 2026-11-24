
from nlp_toolkit.tokenization import tokenize_text

def test_word_tokenization():
    text = "I love Natural Language Processing."

    result = tokenize_text(text)

    assert result == [
        "I",
        "love",
        "Natural",
        "Language",
        "Processing",
        "."
    ]


def test_invalid_input():
    try:
        tokenize_text(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_word_tokenization()
    test_invalid_input()

    print("All tokenization tests passed!")
