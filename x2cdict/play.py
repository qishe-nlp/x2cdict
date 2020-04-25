from x2cdict import VocabDict
import click

@click.command()
@click.option("--word", help="Specify the word to look up", prompt="word")
@click.option("--fromlang", help="Specify the language of the word", prompt="translate from")
@click.option("--tolang", help="Specify the language the word to be translated into", default="zh-cn")
def search_word(word, fromlang, tolang):
  vd = VocabDict(fromlang, tolang)
  r = vd.word(word, "---")
  print(r.text)
