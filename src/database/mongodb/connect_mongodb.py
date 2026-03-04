from pymongo import MongoClient

uri = "mongodb://nraboy:password1234@localhost:27017"
client = MongoClient(uri)
try:

    client.deployments.command("ping")
    print("Connected successfully to", client.get_database('deployments'))
    client.close()

except Exception as e:
    raise Exception(
        "The received error is: ", e
    )
