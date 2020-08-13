from googletrans import Translator
from x2cdict.db import DB
from x2cdict.pos_map import POSMAP
import os

class VocabDict:

  APIS = ["es2cn"]

  def __init__(self, from_lang, to_lang="cn"):
    self.from_lang = from_lang
    self.to_lang = to_lang
    self.dictname = "{}2{}".format(self.from_lang, self.to_lang)
    self.google_api = Translator()
    self.api = None
    if self.dictname in self.__class__.APIS:
      self.api = DB(self.dictname, os.getenv("DB_USER", "phoenix"), os.getenv("DB_PASS", "turingmachine"), os.getenv("DB_HOST", "127.0.0.1"))
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
    try:
      _r = self.google_api.translate(w, src=self.from_lang, dest=to_lang)
      _pos = pos.lower() + "." if pos != None else None 
      result = {
        "word": w,
        "explanation": {"pos": _pos, "meaning": _r.text},
        "from": "Google"
      }
    except Exception as e:
      result = None
    return result

  def api_search_verb_original(self, w, _pos):
    result = None
    verb = self.api.search_vocab(w)
    if verb != None:
      ex = verb["explanation"]

      e = None
      for i in ex:
        if i["pos"] in _pos:
          e = i
          break
 
      if e != None:
        result = {
          "word": w,
          "explanation": e,
          "variations": {
            "origin": w
          },
          "from": self.dictname 
        }

        vv = self.api.search_verbs_variation(w) 
        if vv != None:
          result["extension"] = vv["extension"] 

      return result

  def api_search_verb_variation(self, w, _pos):
    verb = self.api.search_verbs_inverse_variation(w)
    result = None
    if verb != None:
      origin_verb = verb["extension"]["origin"]
      info = self.api_search_verb_original(origin_verb, _pos)
      if info != None:
        result = {
          "word": w,
          "explanation": info["explanation"],
          "variations": {
            "origin": origin_verb,
            "formats": verb["extension"]["variations"]
          },
          "from": self.dictname
        }
        if "extension" in info.keys():
          result["extension"] = info["extension"]
    return result

  def api_search(self, w, pos):
    _pos = self.posmap[pos] if pos in self.posmap.keys() else [pos] 

    result = None
    if pos == "VERB" or pos == "AUX":
      result = self.api_search_verb_original(w, _pos)
      if result == None:
        result = self.api_search_verb_variation(w, _pos)
    else:
      _r = self.api.search_vocab(w)

      if _r != None:
        ex = _r["explanation"]

        e = ex[0]
        for i in ex:
          if i["pos"] in _pos:
            e = i
            break
   
        result = {
          "word": w,
          "explanation": e,
          "from": self.dictname 
        }

    return result
