from x2cdict.google import GoogleVocabDict, GooglePhraseDict

def test_vocab_search():
  from_lang, to_lang = "en", "cn"
  google = GoogleVocabDict(from_lang, to_lang)
  word = "happy"
  r = google.search(word, "ADJ")
  print(r)
  assert r["word"] == word
  assert r["dict_pos"] == "adj."
  assert "meaning" in r
  assert r["extension"] == None
  assert r["variations"] == None
  assert r["from"] == "Google"


def test_phrase_search():
  from_lang, to_lang = "en", "cn"
  google = GooglePhraseDict(from_lang, to_lang)
  phrase = "take care"
  r = google.search(phrase)
  print(r)
  assert r["original"] == phrase
  assert r["from"] == "Google"
