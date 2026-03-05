from pydantic import BaseModel


class Database(BaseModel):
    admin_username: str
    database_name: str
