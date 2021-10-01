from pymongo import MongoClient

# Establishing connection to Mongo
client = MongoClient('localhost', 27017)

#creating database
db = client.trial

# Creating and inserting documents
posts = db.posts
