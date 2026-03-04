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
