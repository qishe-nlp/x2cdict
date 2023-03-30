from x2cdict.dictapi import VocabDict, PhraseDict


def test_vocab_search_with_pos():
  from_lang, to_lang = "en", "cn"
  api = VocabDict(from_lang, to_lang)  

  word = "happy"
  # Right PoS, not using external
  r = api.search(word, "ADJ", False)
  print(r)
  assert r["word"] == word
  assert "meaning" in r
  assert "extension" in r
  assert "variations" in r
  assert "dict_pos" in r
  assert "examples" in r
  assert r["from"] == "en2cn"

  # Wrong PoS, not using external
  r = api.search(word, "XXX", False)
  print(r)
  assert r == None

  # Wrong PoS, using external
  r = api.search(word, "XXX", True)
  print(r)
  assert r != None
  assert r["word"] == word
  assert "meaning" in r
  assert "extension" in r
  assert "variations" in r
  assert r["dict_pos"] == "xxx."
  assert r["from"] == "DeepL"

  word = "xxx"
  # Right PoS, not using external
  r = api.search(word, "ADJ", False)
  print(r)
  assert r == None

  # Wrong PoS, not using external
  r = api.search(word, "XXX", False)
  print(r)
  assert r == None

  # Wrong PoS, using external
  r = api.search("", "XXX", True)
  print(r)
  assert r == None
 
