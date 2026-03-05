from conf import mongodb_client


def connect_mongodb() -> None:
    try:
        mongodb_client.deployments.command("ping")
        print("Connected successfully to", mongodb_client.get_database('deployments'))
        mongodb_client.close()

    except Exception as e:
        raise Exception(
            "The received error is: ", e
        )

def create_new_db_in_mongodb(db_name: str) -> None:
    new_db = mongodb_client[db_name]
    collection = new_db.create_collection('')
    collection.insert_one({})
    mongodb_client.close()
    print(mongodb_client.get_database(db_name))
