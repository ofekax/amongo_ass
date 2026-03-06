import datetime
import uuid

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text
from faker import Faker
import psycopg2

from conf import postgres_db_engine
from src.models.deployment.deployment import Base, Deployment

Session = sessionmaker(bind=postgres_db_engine)
session = Session()

Base.metadata.create_all(postgres_db_engine)


def add_deployment_to_the_table() -> None:
    dep1 = Deployment(id=str(uuid.uuid4()), db_name="d11", status="CREATED",
                      username="userq", creation_time=str(datetime.datetime.now()))
    session.add(dep1)
    session.commit()


def insert_deployment_into_deployment_table(db_name: str, username: str) -> None:
    deployment: Deployment = Deployment(id=str(uuid.uuid4()), db_name=db_name, status="CREATED",
                                        username=username, creation_time=str(datetime.datetime.now()))
    session.add(deployment)
    session.commit()
