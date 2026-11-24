
from nlp_toolkit.sentence_tokenization import tokenize_sentences

def test_sentence_tokenization():
    text = "I study NLP. I use Python. I build AI projects."

    result = tokenize_sentences(text)

    assert result == [
        "I study NLP.",
        "I use Python.",
        "I build AI projects."
    ]


def test_empty_text():
    assert tokenize_sentences("") == []
    assert tokenize_sentences("   ") == []


def test_invalid_input():
    try:
        tokenize_sentences(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_sentence_tokenization()
    test_empty_text()
    test_invalid_input()

    print("All sentence tokenization tests passed!")
