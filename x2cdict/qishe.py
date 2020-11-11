from x2cdict.db import DB
from x2cdict.pos_map import POSMAP
from x2cdict.lib import gen_dictname
import os

class QisheVocabDict:

  APIS = ["es2cn"]

  def __init__(self, from_lang, to_lang="cn"):
    self.from_lang, self.to_lang = from_lang, to_lang
    self.dictname = gen_dictname(self.from_lang, self.to_lang) 

    self.api = None
    if self.dictname in self.__class__.APIS:
      self.api = DB(self.dictname, os.getenv("DB_USER", "phoenix"), os.getenv("DB_PASS", "turingmachine"), os.getenv("DB_HOST", "127.0.0.1"))
      self.posmap = POSMAP[self.from_lang]

  def verb_original(self, w, _pos):
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

        vv = self.api.search_verb_variation(w) 
        if vv != None:
          result["extension"] = vv["extension"] 

      return result

  def verb_variation(self, w, _pos):
    verb = self.api.search_verb_inverse_variation(w)
    result = None
    if verb != None:
      origin_verb = verb["extension"]["origin"]
      info = self.verb_original(origin_verb, _pos)
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

  def other_vocab(self, w, _pos):
    _r = self.api.search_vocab(w)

    if _r != None:
      ex = _r["explanation"]

      e = ex[0] # default: first explaination
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

  def search(self, w, pos):
    result = None
    if self.api == None:
      return result

    _pos = self.posmap[pos] if pos in self.posmap.keys() else [pos] 

    if pos == "VERB" or pos == "AUX":
      result = self.verb_original(w, _pos)
      if result == None:
        result = self.verb_variation(w, _pos)
    else:
      result = self.other_vocab(w, _pos)
    return result
