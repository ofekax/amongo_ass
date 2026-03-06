import datetime
import uuid

from src.database.mongodb.connect_to_mongodb import create_new_db_in_mongodb
from src.database.postgres.connect_to_postgres_db import insert_deployment_into_deployment_table
from src.models.db_model import MongodbDatabase
from src.models.deployment.check_deployment import is_good_deployment_data, check_username
from src.models.deployment.deployment import Deployment


def create_deployment(db_name: str, username: str) -> None:
    if is_good_deployment_data(username, db_name):
        username = check_username(username)
        db_data = {'admin_username': username, 'database_name': db_name}
        try:
            mongodb_db: MongodbDatabase = MongodbDatabase(**db_data)
            create_new_db_in_mongodb(mongodb_db)
            deployment: Deployment = Deployment(id=str(uuid.uuid4()), db_name=db_name, status="CREATED",
                                                username=username, creation_time=str(datetime.datetime.now()))
            insert_deployment_into_deployment_table(deployment)
        except Exception as e:
            raise Exception(
                "The received error is: ", e
            )
