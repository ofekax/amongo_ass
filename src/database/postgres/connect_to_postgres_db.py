
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text
from faker import Faker
import psycopg2


db_engine = create_engine('postgresql://postgres:secret@deployments_metadata:5432/deployments')


Session = sessionmaker(bind=db_engine)
session = Session()


