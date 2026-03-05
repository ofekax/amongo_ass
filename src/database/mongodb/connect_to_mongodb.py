from conf import mongodb_client
from src.models.db_model import MongodbDatabase


def connect_mongodb() -> None:
    try:
        mongodb_client.deployments.command("ping")
        print("Connected successfully to", mongodb_client.get_database('deployments'))
        mongodb_client.close()

    except Exception as e:
        raise Exception(
            "The received error is: ", e
        )

def create_new_db_in_mongodb(mongodb_db: MongodbDatabase) -> None:
    new_db = mongodb_client[mongodb_db.database_name]
    collection = new_db.create_collection(mongodb_db.collection)
    collection.insert_one(mongodb_db.collection_doc)
    mongodb_client.close()

