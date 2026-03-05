from pydantic import BaseModel


class MongodbDatabase(BaseModel):
    admin_username: str
    database_name: str
    collection: str
    collection_doc: dict


