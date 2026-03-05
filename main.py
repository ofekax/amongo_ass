# This is a sample Python script.
from src.database.postgres.connect_to_postgres_db import db_engine
from src.database.postgres.postgressql_and_padmin_settings import compose_file_setting
from src.models.deployment.deployment_notgood import Deployment


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main() -> None:
    db = db_engine
    print(db)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
