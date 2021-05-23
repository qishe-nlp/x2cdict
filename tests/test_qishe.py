from x2cdict.qishe import QisheVocabDict

def test_en_vocab_search_with_pos():
  from_lang, to_lang = "en", "cn"
  qishe = QisheVocabDict(from_lang, to_lang)
  word = "happy"
  r = qishe.search_with_pos(word, "ADJ")
  print(r)
  assert r["word"] == word
  assert "dict_pos" in r
  assert "meaning" in r
  assert "extension" in r
  assert "variations" in r
  assert "examples" in r
  assert r["from"] == "en2cn"


def test_es_vocab_search_with_pos():
  from_lang, to_lang = "es", "cn"
  qishe = QisheVocabDict(from_lang, to_lang)
  word = "trabajo"
  r = qishe.search_with_pos(word, "VERB")
  print(r)
  assert r["word"] == word
  assert "dict_pos" in r
  assert "meaning" in r
  assert "extension" in r
  assert "variations" in r
  assert "examples" in r
  assert r["from"] == "es2cn"


def test_en_vocab_search_without_pos():
  from_lang, to_lang = "en", "cn"
  qishe = QisheVocabDict(from_lang, to_lang)
  word = "happy"
  r = qishe.search_without_pos(word)
  print(r)
  assert "word" in r
  assert "explanation" in r
  assert "dict_pos" not in r
  assert "from" not in r

def test_es_vocab_search_without_pos():
  from_lang, to_lang = "es", "cn"
  qishe = QisheVocabDict(from_lang, to_lang)
  word = "trabajo"
  r = qishe.search_without_pos(word)
  print(r)
  assert "word" in r
  assert "explanation" in r
  assert "dict_pos" not in r
  assert "from" not in r

