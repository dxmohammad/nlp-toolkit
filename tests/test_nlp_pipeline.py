
from nlp_toolkit.nlp_pipeline import process_text

def test_pipeline():
    text = (
        "Elon Musk founded SpaceX. "
        "He works on artificial intelligence."
    )

    result = process_text(text)

    expected_keys = {
        "cleaned_text",
        "normalized_text",
        "tokens",
        "filtered_tokens",
        "stemmed_tokens",
        "sentences",
        "lemmas",
        "pos_tags",
        "entities"
    }

    assert set(result.keys()) == expected_keys

    # Check output types
    assert isinstance(result["cleaned_text"], str)
    assert isinstance(result["normalized_text"], str)

    for key in [
        "tokens",
        "filtered_tokens",
        "stemmed_tokens",
        "sentences",
        "lemmas",
        "pos_tags",
        "entities"
    ]:
        assert isinstance(result[key], list)

    # Check preprocessing
    assert result["normalized_text"] == (
        result["normalized_text"].lower()
    )

    assert len(result["tokens"]) > 0

    # Check consistency between processing stages
    assert len(result["stemmed_tokens"]) == len(
        result["filtered_tokens"]
    )

    # Check sentence tokenization
    assert len(result["sentences"]) == 2

    # Check POS Tagging structure
    assert all(
        isinstance(item, tuple) and len(item) == 2
        for item in result["pos_tags"]
    )

    # Check NER structure
    assert all(
        set(entity.keys()) == {"text", "label", "description"}
        for entity in result["entities"]
    )


def test_empty_input():
    try:
        process_text("")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")


def test_whitespace_input():
    try:
        process_text("     ")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")


def test_invalid_input():
    try:
        process_text(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_pipeline()
    test_empty_input()
    test_whitespace_input()
    test_invalid_input()

    print("All NLP Pipeline tests passed!")
