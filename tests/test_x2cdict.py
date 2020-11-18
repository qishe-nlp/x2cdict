from x2cdict import __version__, VocabDict


def test_version():
  assert __version__ == '0.1.25'


def test_es2cn():
  fromlang, tolang = "es", "cn"
  word = "hehehe"
  pos = None
  google = False
  vd = VocabDict(fromlang, tolang)
  r = vd.search(word, pos, google)
  print("Hello")
  print(r)
  assert r == None
