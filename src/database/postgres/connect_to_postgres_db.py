
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text
from faker import Faker
import psycopg2

from conf import postgres_db_engine
from src.models.deployment.deployment import Base, Deployment

Session = sessionmaker(bind=postgres_db_engine)
session = Session()

def create_deployment_table() -> None:
    Base.metadata.create_all(postgres_db_engine)

def insert_deployment_into_deployment_table(deployment: Deployment) -> None:
    new_row: Deployment = deployment
    session.add(deployment)
    session.commit()





