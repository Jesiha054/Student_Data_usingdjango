from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/')
db=con['intern']
col=db['data']
print("connect")