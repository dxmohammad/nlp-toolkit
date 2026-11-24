import unittest
from unittest.mock import patch

from nlp_toolkit._nltk import ensure_nltk_resource


class TestNLTKResources(unittest.TestCase):

    @patch("nlp_toolkit._nltk.nltk.data.find")
    def test_resource_exists(self, mock_find):
        ensure_nltk_resource("punkt_tab")

        mock_find.assert_called_once_with(
            "tokenizers/punkt_tab/english/"
        )

    @patch("nlp_toolkit._nltk.nltk.data.find")
    def test_missing_resource(self, mock_find):
        mock_find.side_effect = LookupError

        with self.assertRaisesRegex(
            LookupError,
            "Required NLTK resource"
        ):
            ensure_nltk_resource("punkt_tab")

    def test_unknown_resource(self):
        with self.assertRaises(ValueError):
            ensure_nltk_resource("unknown_resource")


if __name__ == "__main__":
    unittest.main()