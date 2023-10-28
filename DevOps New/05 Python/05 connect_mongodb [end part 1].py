import pymongo
import pymongoarrow
from pymongo import MongoClient
import pprint
client = MongoClient('mongodb+srv://tmtdbAdmin:LQCVpi0yiJd0iICl@tmtdb.alrrmch.mongodb.net/')

db = client.activities
col = db.records

for doc in col.find({}):
  pprint.pprint(doc)