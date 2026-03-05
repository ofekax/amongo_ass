
from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text
from faker import Faker
import psycopg2

from src.models.deployment.deployment import Base

db_engine = create_engine('postgresql://postgres:secret@localhost:5432/deployments')


Session = sessionmaker(bind=db_engine)
session = Session()

def create_deployment_table() -> None:
    Base.metadata.create_all(db_engine)



