from googletrans import Translator

def reform_pos(pos):
  return pos.lower() + "." if pos != None else None

class GoogleVocabDict:

  def __init__(self, from_lang, to_lang="zh-cn"):
    self.from_lang, self.to_lang = from_lang, "zh-cn" if to_lang == "cn" else to_lang 
    self.api = Translator()

  def search(self, w, pos):
    try:
      _r = self.api.translate(w, src=self.from_lang, dest=self.to_lang)
      _pos = reform_pos(pos)
      result = {
        "word": w,
        "explanation": {"pos": _pos, "meaning": _r.text},
        "from": "Google"
      }
    except Exception as e:
      result = None
    return result


