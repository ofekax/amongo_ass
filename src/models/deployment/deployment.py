import datetime

import uuid

from conf import db
from src.models.deployment.check_deployment import check_username




class Deployment:
    def __init__(self, username: str):
        self.id: str = str(uuid.uuid4())
        self.db_name: str = username + db.name
        self.status: str = 'CREATED'
        self.username = username
        self.creation_time: datetime = datetime.datetime.now()
        self.username: str = check_username(username)
