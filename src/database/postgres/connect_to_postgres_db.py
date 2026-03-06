import datetime
import uuid

from sqlalchemy.orm import Session, sessionmaker
from conf import postgres_db_engine
from src.models.deployment.deployment import Base, Deployment

Session = sessionmaker(bind=postgres_db_engine)
session = Session()

Base.metadata.create_all(postgres_db_engine)

def insert_deployment_into_deployment_metadata_table(db_name: str, username: str) -> None:
    deployment: Deployment = Deployment(id=str(uuid.uuid4()), db_name=db_name, status="CREATED",
                                        username=username, creation_time=str(datetime.datetime.now()))
    session.add(deployment)
    session.commit()
