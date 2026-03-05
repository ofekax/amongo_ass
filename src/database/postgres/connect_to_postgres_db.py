import logging
from sqlalchemy import create_engine
from sqlalchemy import text
from faker import Faker
import psycopg2

def get_postgres_db_engine():
    return create_engine('postgresql://postgres:secret@postgres-service:5432/deployments')


db_engine = get_postgres_db_engine().connect()
