from src.database.mongodb.connect_to_mongodb import create_new_db_in_mongodb
from src.database.postgres.connect_to_postgres_db import insert_deployment_into_deployment_metadata_table
from src.models.db_model import MongodbDatabase
from src.models.deployment.check_deployment import is_good_deployment_data, check_username
from src.models.deployment.deployment import Deployment


def create_deployment(deployment: Deployment) -> None:
    if is_good_deployment_data(deployment.username, deployment.db_name):
        username = check_username(deployment.username)
        db_data = {'admin_username': username, 'database_name': deployment.db_name}
        try:
            mongodb_db: MongodbDatabase = MongodbDatabase(**db_data)
            create_new_db_in_mongodb(mongodb_db)

            insert_deployment_into_deployment_metadata_table(deployment.db_name, username)
        except Exception as e:
            raise Exception(
                "The received error is: ", e
            )
