from pymongo import MongoClient

uri = "mongodb://nraboy:password1234@localhost:27017"
mongodb_client = MongoClient(uri)
db = mongodb_client["deployments"]

