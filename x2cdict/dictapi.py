from x2cdict.google import GoogleVocabDict
from x2cdict.qishe import QisheVocabDict

class VocabDict:
  """
  It combines qishe and google voacb api
  """

  def __init__(self, from_lang, to_lang="cn"):
    self.from_lang, self.to_lang = from_lang, to_lang
    self.google_api = GoogleVocabDict(from_lang, to_lang)
    self.qishe_api = QisheVocabDict(from_lang, to_lang)

  def search(self, w, pos=None, google=True):
    result = self.qishe_api.search(w, pos)
    if result == None:
      result = self.google_api.search(w, pos) if google else None
    return result
