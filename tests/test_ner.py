
from nlp_toolkit.ner import extract_entities

def test_extract_entities():
    text = "Elon Musk founded SpaceX in the United States."

    result = extract_entities(text)

    assert isinstance(result, list)
    assert len(result) > 0

    assert all(
        set(entity.keys()) == {"text", "label", "description"}
        for entity in result
    )

    entity_names = [
        entity["text"]
        for entity in result
    ]

    assert "Elon Musk" in entity_names


def test_entity_structure():
    result = extract_entities("Apple is a company.")

    for entity in result:
        assert isinstance(entity["text"], str)
        assert isinstance(entity["label"], str)
        assert isinstance(entity["description"], str)


def test_empty_text():
    assert extract_entities("") == []


def test_invalid_input():
    try:
        extract_entities(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_extract_entities()
    test_entity_structure()
    test_empty_text()
    test_invalid_input()

    print("All NER tests passed!")
