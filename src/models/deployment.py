import datetime

from pydantic import BaseModel
import uuid

@BaseModel
class Deployment:
    id: str = str(uuid.uuid4())
    db_name: str
    #שם ה-database  שלכם חייב להתחיל עם prefix של ה user
    status: str
    username: str
    #אם היוזר שלכם הינו יוזר חד ספרתי יש להוסיף 0 לפני הספרה
    creation_time: datetime = datetime.datetime.now()








