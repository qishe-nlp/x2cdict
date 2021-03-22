from x2cdict.posmap import POSMAP

def test_POSMAP():
  assert "en" in POSMAP
  assert "es" in POSMAP
  assert "jp" not in POSMAP
  assert "fr" not in POSMAP
  assert "de" not in POSMAP
  assert "it" not in POSMAP
