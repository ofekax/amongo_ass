# This is a sample Python script.
from src.database.mongodb.connect_to_mongodb import create_new_db_in_mongodb
from src.models.db_model import MongodbDatabase
from src.rest_api.croud.create import create_deployment


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main() -> None:

    create_deployment('userq_best', 'userq')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
