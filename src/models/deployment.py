import datetime

from pydantic import BaseModel
import uuid

@BaseModel
class Deployment:
    id: str = str(uuid.uuid4())
    db_name: str
    status: str
    username: str
    creation_time: datetime = datetime.datetime.now()




