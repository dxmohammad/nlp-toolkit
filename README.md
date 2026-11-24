# NLP Toolkit

A modular Python toolkit for Natural Language Processing (NLP), providing reusable functions for common text preprocessing, linguistic analysis, and text vectorization tasks.

The project is designed with a modular structure, allowing developers to use individual NLP functions or combine them into a complete text-processing pipeline.

**PyPI:** [dxmohammad-nlp-toolkit](https://pypi.org/project/dxmohammad-nlp-toolkit/)
**GitHub:** [nlp-toolkit](https://github.com/dxmohammad/nlp-toolkit)

## Features

The toolkit currently includes 11 modules:

| Module | Description |
|---|---|
| `cleaning` | Provides text-cleaning operations for punctuation and unwanted characters |
| `normalization` | Normalizes text and whitespace |
| `tokenization` | Splits text into individual words |
| `stopwords` | Removes stopwords while preserving negation words |
| `stemming` | Applies Porter Stemming |
| `lemmatization` | Converts words into their base forms using spaCy |
| `pos_tagging` | Performs Part-of-Speech tagging |
| `ner` | Extracts Named Entities from text |
| `sentence_tokenization` | Splits text into sentences |
| `vectorization` | Supports Bag of Words and TF-IDF |
| `nlp_pipeline` | Combines multiple NLP operations into one pipeline |

## Project Structure

```text
nlp-toolkit/
â”‚
â”œâ”€â”€ nlp_toolkit/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ _nltk.py
â”‚   â”œâ”€â”€ _spacy.py
â”‚   â”œâ”€â”€ cleaning.py
â”‚   â”œâ”€â”€ normalization.py
â”‚   â”œâ”€â”€ tokenization.py
â”‚   â”œâ”€â”€ stopwords.py
â”‚   â”œâ”€â”€ stemming.py
â”‚   â”œâ”€â”€ lemmatization.py
â”‚   â”œâ”€â”€ pos_tagging.py
â”‚   â”œâ”€â”€ ner.py
â”‚   â”œâ”€â”€ sentence_tokenization.py
â”‚   â”œâ”€â”€ vectorization.py
â”‚   â””â”€â”€ nlp_pipeline.py
â”‚
â”œâ”€â”€ tests/
â”‚   â”œâ”€â”€ test_cleaning.py
â”‚   â”œâ”€â”€ test_lemmatization.py
â”‚   â”œâ”€â”€ test_ner.py
â”‚   â”œâ”€â”€ test_nlp_pipeline.py
â”‚   â”œâ”€â”€ test_nltk_resources.py
â”‚   â”œâ”€â”€ test_normalization.py
â”‚   â”œâ”€â”€ test_pos_tagging.py
â”‚   â”œâ”€â”€ test_sentence_tokenization.py
â”‚   â”œâ”€â”€ test_stemming.py
â”‚   â”œâ”€â”€ test_stopwords.py
â”‚   â”œâ”€â”€ test_tokenization.py
â”‚   â””â”€â”€ test_vectorization.py
â”‚
â”œâ”€â”€ .gitignore
â”œâ”€â”€ LICENSE
â”œâ”€â”€ README.md
â”œâ”€â”€ pyproject.toml
â””â”€â”€ requirements.txt
```

## Requirements

- Python 3.10 or later.
- NLTK
- spaCy
- scikit-learn
- SciPy

## Installation

### 1. Install from PyPI (Recommended)

Install the latest published version using pip:

```bash
pip install dxmohammad-nlp-toolkit
```

### 2. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 3. Download NLTK resources

Some modules require additional NLTK language resources.

Download the required resources using:

```python
import nltk

nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger_eng")
```

These resources are required by the relevant tokenization, stopword removal, and POS tagging modules.

### 4. Install from source (Development)

If you want to access or modify the source code:

```bash
git clone https://github.com/dxmohammad/nlp-toolkit.git
cd nlp-toolkit
pip install .
```

## Usage

### 1. Text Cleaning

```python
from nlp_toolkit.cleaning import clean_text

text = "Hello, World! NLP is interesting."
result = clean_text(text)

print(result)
```

### 2. Text Normalization

```python
from nlp_toolkit.normalization import normalize_text

text = "  HELLO    WORLD  "
result = normalize_text(text)

print(result)
```

### 3. Word Tokenization

```python
from nlp_toolkit.tokenization import tokenize_text

text = "I love Natural Language Processing."
tokens = tokenize_text(text)

print(tokens)
```

### 4. Stopword Removal

```python
from nlp_toolkit.stopwords import remove_stopwords

text = "This is an example of text processing."
result = remove_stopwords(text)

print(result)
```

### 5. Stemming

```python
from nlp_toolkit.stemming import stem_words

words = ["playing", "studies", "running"]
result = stem_words(words)

print(result)
```

### 6. Lemmatization

```python
from nlp_toolkit.lemmatization import lemmatize_text

text = "The children are playing."
result = lemmatize_text(text)

print(result)
```

### 7. Part-of-Speech Tagging

```python
from nlp_toolkit.pos_tagging import get_pos_tags

text = "The researchers develop intelligent systems."
result = get_pos_tags(text)

print(result)
```

### 8. Named Entity Recognition

```python
from nlp_toolkit.ner import extract_entities

text = "Elon Musk founded SpaceX."
result = extract_entities(text)

print(result)
```

### 9. Sentence Tokenization

```python
from nlp_toolkit.sentence_tokenization import tokenize_sentences

text = "NLP is interesting. Python is useful."
result = tokenize_sentences(text)

print(result)
```

### 10. Text Vectorization

**Bag of Words**

```python
from nlp_toolkit.vectorization import bag_of_words

documents = [
    "I love machine learning",
    "Machine learning is interesting"
]

matrix, vocabulary = bag_of_words(documents)

print(matrix.toarray())
print(vocabulary)
```

**TF-IDF**

```python
from nlp_toolkit.vectorization import tfidf_vectorization

documents = [
    "I love machine learning",
    "Machine learning is interesting"
]

matrix, vocabulary = tfidf_vectorization(documents)

print(matrix.toarray())
print(vocabulary)
```

### 11. Complete NLP Pipeline

```python
from nlp_toolkit.nlp_pipeline import process_text

text = "Elon Musk is developing artificial intelligence."

result = process_text(text)

for key, value in result.items():
    print(f"{key}: {value}")
```

## Testing

The project includes 12 individual test files.

To run all tests from the project root directory using PowerShell:

```powershell
$python = "python"
$env:PYTHONPATH = (Get-Location).Path

try {
    $testFiles = Get-ChildItem .\tests -Filter "test_*.py" -File | Sort-Object Name

    foreach ($test in $testFiles) {
        Write-Host "Testing $($test.Name)"

        & $python $test.FullName

        if ($LASTEXITCODE -ne 0) {
            throw "Test failed: $($test.Name)"
        }
    }

    Write-Host "ALL PROJECT TESTS PASSED!"
}
finally {
    Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
}
```

## Technologies Used

- Python
- NLTK
- spaCy
- scikit-learn
- SciPy

## Project Status

Version `0.1.0` has been successfully published on PyPI.

The initial implementation of the toolkit is complete, with:

- 11 functional NLP modules.
- 12 individual test files.
- Modular NLTK resource management.
- Cached spaCy model loading.
- Package configuration using `pyproject.toml`.
- Wheel and source distribution builds.
- Successful installation testing in an independent Python environment.
- Successful publication and installation testing through PyPI and TestPyPI.

**Current PyPI Version:** `0.1.0`

**Installation:**

```bash
pip install dxmohammad-nlp-toolkit
```

## Future Improvements

- Expand language support.
- Add more text preprocessing techniques.
- Improve pipeline flexibility.
- Expand automated test coverage.
- Add automated testing using GitHub Actions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Mohammad**

GitHub: [@dxmohammad](https://github.com/dxmohammad)

Project Repository: [nlp-toolkit](https://github.com/dxmohammad/nlp-toolkit)

**PyPI:** [dxmohammad-nlp-toolkit](https://pypi.org/project/dxmohammad-nlp-toolkit/)
