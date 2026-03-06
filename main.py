# This is a sample Python script.
from src.database.postgres.connect_to_postgres_db import  \
    insert_deployment_into_deployment_table
from src.models.db_model import MongodbDatabase
from src.rest_api.croud.create import add_deployment


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main() -> None:
    insert_deployment_into_deployment_table("userthe_best", "userrr")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
