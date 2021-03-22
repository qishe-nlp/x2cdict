# Installation

```
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose x2cdict 
```

# Usage
### Environment setting

* `DICT_DB_HOST` is `127.0.0.1` by default
* `DICT_DB_USER` is `dict` by default
* `DICT_DB_PASS` is `turingmachine` by default


The dictionary db is not built in this project, you have to install the DB by yourself, refer to [BaJiu Dictionary Installation](https://github.com/bajiu-dict/deploy_dict_mongo).

### Binary Usage

* Search vocabs with PoS assgined
```
vocab --fromlang en --tolang cn --pos ADJ --word happy --google False
vocab --help
```

* Search vocabs without PoS
```
vocab_without_pos --fromlang en --tolang cn --word happy --google False
vocab_without_pos --help
```

* Search phrase
```
phrase --fromlang en --tolang cn --phrase "overcome the problem"
phrase --help
```

### Package Usage
```
from x2cdict import VocabDict, PhraseDict
def search_vocab(word, pos, fromlang, tolang, google):
  vd = VocabDict(fromlang, tolang)
  r = vd.search(word, pos, google)
  print(r)

def search_vocab_without_pos(word, fromlang, tolang, google):
  vd = VocabDict(fromlang, tolang)
  r = vd.search_without_pos(word, google)
  print(r)

def search_phrase(phrase, fromlang, tolang):
  vd = PhraseDict(fromlang, tolang)
  r = vd.search(phrase)
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

### Test
```
poetry run pytest -rP
```
which run tests under `tests/*`

### Execute
```
poetry run vocab --help
poetry run vocab_without_pos --help
poetry run phrase --help
```

### Build
* Change `version` in
  * `pyproject.toml`
  * `x2cdict/__init__.py`
  * `tests/test_x2cdict.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`

# TODO:

### Github action to publish package
* pypi test repo
* pypi repo
