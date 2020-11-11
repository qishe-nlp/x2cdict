from pymongo import MongoClient
from urllib.parse import quote_plus

class DB:
  """
  Encapsulation of mongodb
  """
  def __init__(self, dbname, user, password, host, authdb='admin'):
    uri = "mongodb://{}:{}@{}/{}".format(quote_plus(user), quote_plus(password), host, authdb)
    self.client = MongoClient(uri)
    self.db = self.client[dbname]
    self.vocabs = self.db.vocabs
    # TODO: the collections should be varied among different languages
    self.verbs_variation = self.db.verbs_variation
    self.verbs_inverse_variation = self.db.verbs_inverse_variation

  def search_vocab(self, text):
    result = self.vocabs.find_one({"word": text})
    return result 

  def search_verb_variation(self, text):
    result = self.verbs_variation.find_one({"word": text})
    return result 

  def search_verb_inverse_variation(self, text):
    result = self.verbs_inverse_variation.find_one({"word": text})
    return result 

