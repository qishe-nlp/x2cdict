from googletrans import Translator
from x2cdict.db import DB
from x2cdict.pos_map import POSMAP

class VocabDict:

  APIS = ["es2cn"]

  def __init__(self, from_lang, to_lang="cn"):
    self.from_lang = from_lang
    self.to_lang = to_lang
    self.dictname = "{}2{}".format(self.from_lang, self.to_lang)
    self.google_api = Translator()
    self.api = None
    if self.dictname in self.__class__.APIS:
      # TODO: move auth into configuration
      self.api = DB(self.dictname, "phoenix", "turingmachine", "192.168.21.2")
      self.posmap = POSMAP[from_lang]

  def word(self, w, pos=None):
    if self.api != None:
      result = self.api_search(w, pos)
      if result == None:
        result = self.google_search(w, pos)
    else:
      result = self.google_search(w, pos)
    return result

  def google_search(self, w, pos):
    to_lang = self.to_lang
    if self.to_lang == "cn":
      to_lang = "zh-cn"
    _r = self.google_api.translate(w, src=self.from_lang, dest=to_lang)
    _pos = pos.lower() + "." if pos != None else None 
    result = {
      "word": w,
      "explaination": {"pos": _pos, "meaning": _r.text},
      "from": "Google"
    }
    return result

  def api_search(self, w, pos):
    _pos = self.posmap[pos] if pos in self.posmap.keys() else [pos] 
    _r = self.api.search_vocab(w)

    result = None
    if _r != None:
      ex = _r["explaination"]

      e = ex[0]
      for i in ex:
        if i["pos"] in _pos:
          e = i
          break
 
      result = {
        "word": w,
        "explaination": e,
        "from": self.dictname 
      }
    return result
