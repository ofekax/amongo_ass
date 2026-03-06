import datetime
import uuid

from conf import mongodb_client
from src.database.postgres.connect_to_postgres_db import session
from src.models.db_model import MongodbDatabase
from src.models.deployment.check_deployment import is_good_deployment_data, check_username
from src.models.deployment.deployment import Deployment


def create_new_db_in_mongodb(mongodb_db: MongodbDatabase) -> None:
    new_db = mongodb_client[mongodb_db.database_name]
    collection = new_db.create_collection(mongodb_db.collection)
    collection.insert_one(mongodb_db.collection_doc)
    mongodb_client.close()


def insert_deployment_into_deployment_metadata_table(deployment: Deployment) -> None:
    session.add(deployment)
    session.commit()


def create_deployment(db_name: str, username: str) -> None:
    if is_good_deployment_data(username, db_name):
        username = check_username(username)
        db_data = {'admin_username': username, 'database_name': db_name}
        deployment_metadata = {'id': uuid.uuid4(), 'db_name': db_name, 'status': 'CREATED', 'username': username,
                               'creation_time': datetime.datetime.now()}
        try:
            mongodb_db: MongodbDatabase = MongodbDatabase(**db_data)
            create_new_db_in_mongodb(mongodb_db)
            deployment_metadata: Deployment = Deployment()
            insert_deployment_into_deployment_metadata_table(deployment_metadata)
        except Exception as e:
            raise Exception(
                "The received error is: ", e
            )
