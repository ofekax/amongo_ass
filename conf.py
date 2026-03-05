from pymongo import MongoClient
from sqlalchemy import create_engine

uri = "mongodb://nraboy:password1234@localhost:27017"
mongodb_client = MongoClient(uri)

postgres_db_engine = create_engine('postgresql://postgres:secret@localhost:5432/deployments')




