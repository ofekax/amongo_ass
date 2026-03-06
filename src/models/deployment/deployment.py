from sqlalchemy import String, Column
import datetime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Deployment(Base):
    __tablename__ = 'deployments_metadata'

    id: str = Column(String, primary_key=True)
    db_name: str = Column(String)
    status: str = Column(String(50))
    username: str = Column(String(50))
    creation_time: datetime = Column(String)

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, db_name={self.db_name!r}, status={self.status!r}, username={self.username!r}, "
                f"creation_time={self.creation_time!r})")
