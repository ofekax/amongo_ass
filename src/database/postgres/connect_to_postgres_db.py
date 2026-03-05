
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text
from faker import Faker
import psycopg2

from conf import postgres_db_engine
from src.models.deployment.deployment import Base


Session = sessionmaker(bind=postgres_db_engine)
session = Session()

def create_deployment_table() -> None:
    Base.metadata.create_all(postgres_db_engine)



