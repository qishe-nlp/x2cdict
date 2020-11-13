# Installation

```
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose x2cdict 
```

# Usage

### Binary Usage

```
vocab --fromlang en --tolang cn --word happy
vocab --help
```

### Package Usage
```
from x2cdict import VocabDict
def search_vocab(word, pos, fromlang, tolang, google):
  vd = VocabDict(fromlang, tolang)
  r = vd.search(word, pos, google)
  print(r)
```

From above, `google` is a boolean variable to switch whether using google translation, default is `True`.


# Development

### Clone the project
```
git clone https://github.com/qishe-nlp/x2cdict.git
```

### Install [poetry](https://python-poetry.org/docs/)

### Install dependencies
```
poetry update
```

### Execute
```
poetry run vocab --help
```

### Build
* Change `version` in `pyproject.toml` and `x2cdict/__init__.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`


# TODO

### Test and Issue
* `tests/*`

### Github action to publish package
* pypi test repo
* pypi repo
