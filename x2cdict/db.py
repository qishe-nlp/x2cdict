from pymongo import MongoClient

class DB:
  def __init__(self, dbname):
    self.client = MongoClient()
    self.db = self.client[dbname]
    self.vocabs = self.db.vocabs

  def search_vocab(self, text):
    result = self.vocabs.find_one({"word": text})
    return result 
