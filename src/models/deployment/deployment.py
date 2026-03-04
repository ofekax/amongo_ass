import datetime

from pydantic import BaseModel
import uuid

from conf import db


class Deployment:
    def __int__(self, status: str, username: str):
        self.id: str = str(uuid.uuid4())
        self.db_name: str = username + db.name
        self.status: str = 'CREATED'
        self.username = username
        self.creation_time: datetime = datetime.datetime.now()
        username: str
        # אם היוזר שלכם הינו יוזר חד ספרתי יש להוסיף 0 לפני הספרה



