class VocabDict:

  def __init__(self, from_lang, to_lang="zh-cn"):
    self.from_lang = from_lang
    self.to_lang = to_lang

  def word(self, w, pos):
    from googletrans import Translator
    api = Translator()
    return api.translate(w, src=self.from_lang, dest=self.to_lang)

