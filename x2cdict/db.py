from pymongo import MongoClient
from urllib.parse import quote_plus

class DB:
  def __init__(self, dbname, user, password, host, authdb='admin'):
    uri = "mongodb://{}:{}@{}/{}".format(quote_plus(user), quote_plus(password), host, authdb)
    self.client = MongoClient(uri)
    self.db = self.client[dbname]
    self.vocabs = self.db.vocabs

  def search_vocab(self, text):
    result = self.vocabs.find_one({"word": text})
    return result 
