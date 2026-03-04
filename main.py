# This is a sample Python script.
from src.models.deployment.deployment import Deployment


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main() -> None:
    username: str = "user2"
    deployment: Deployment = Deployment(username=username)
    print(deployment.username)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
