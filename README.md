# NLP Toolkit

A Python toolkit for Natural Language Processing (NLP), providing reusable functions for common text preprocessing and analysis tasks.

## Features

The toolkit currently includes 11 modules:

| Module | Description |
|---|---|
| `cleaning` | Removes punctuation, numbers, and unnecessary characters |
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
nlp_tokens/
│
├── nlp_toolkit/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── normalization.py
│   ├── tokenization.py
│   ├── stopwords.py
│   ├── stemming.py
│   ├── lemmatization.py
│   ├── pos_tagging.py
│   ├── ner.py
│   ├── sentence_tokenization.py
│   ├── vectorization.py
│   └── nlp_pipeline.py
│
├── tests/
│   ├── test_cleaning.py
│   ├── test_normalization.py
│   ├── test_tokenization.py
│   ├── test_stopwords.py
│   ├── test_stemming.py
│   ├── test_lemmatization.py
│   ├── test_pos_tagging.py
│   ├── test_ner.py
│   ├── test_sentence_tokenization.py
│   ├── test_vectorization.py
│   └── test_nlp_pipeline.py
│
└── README.md
```

## Requirements

- Python 3.10 or later
- NLTK
- spaCy
- scikit-learn
- SciPy

## Installation

Clone the repository:

```bash
git clone git clone https://github.com/dxmohammad/nlp-toolkit.git
cd nlp-toolkit
```

Install the required libraries:

```bash
pip install nltk spacy scikit-learn scipy
```

Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

Some NLTK modules require additional language resources. Download the resources required by the relevant modules before using them.

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

**Bag of Words:**

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

**TF-IDF:**

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

Run all tests from the project root directory using PowerShell:

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

## Technologies Used

- Python
- NLTK
- spaCy
- scikit-learn
- SciPy

## Project Status

The initial implementation of the toolkit is complete.

All 11 individual test files have passed after organizing the project into a Python package.

## Future Improvements

- Expand language support.
- Add more text preprocessing techniques.
- Improve pipeline flexibility.
- Add more automated tests.
- Prepare the toolkit for package distribution.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
