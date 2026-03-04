from pymongo import MongoClient


uri = "mongodb://nraboy:password1234@localhost:27017/"
client = MongoClient(uri)
try:

    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The received error is: ", e
    )
