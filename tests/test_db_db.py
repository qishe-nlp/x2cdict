from x2cdict.db.db import DB
import pytest


def test_db_with_exception():

  dbname = ""
  user = ""
  password = ""
  host = ""
  authdb = ""

  with pytest.raises(Exception):
    db = DB(dbname, user, password, host, authdb)


def test_db_with_wrong_auth():
  dbname = "xxx"
  user = "xxx"
  password = "xxx"
  host = "127.0.0.1"
  authdb = "admin"
  db = DB(dbname, user, password, host, authdb)

  print(db.db)
  print(db.client)
  # TODO: The auth issue can only be found when the query API is called, it should be checked during connection
  with pytest.raises(Exception):
    db.db.vocabs.find_one({"word": "xxx"})
