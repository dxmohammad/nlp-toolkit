from nlp_toolkit.pos_tagging import get_pos_tags


def test_pos_tagging():
    text = "The intelligent student studies AI"

    result = get_pos_tags(text)

    assert isinstance(result, list)
    assert all(
        isinstance(item, tuple) and len(item) == 2
        for item in result
    )

    assert result[0][0] == "The"


def test_empty_text():
    assert get_pos_tags("") == []


def test_invalid_input():
    try:
        get_pos_tags(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")


if __name__ == "__main__":
    test_pos_tagging()
    test_empty_text()
    test_invalid_input()

    print("All POS Tagging tests passed!")
