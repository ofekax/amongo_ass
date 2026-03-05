from sqlalchemy import String, Column, UUID, DateTime
import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.database.postgres.connect_to_postgres_db import db_engine


class Base(DeclarativeBase):
    pass


class Deployment(Base):
    __tablename__ = 'deployments_metadata'

    id: str = Column(UUID, primary_key=True)
    db_name: str = Column(String(50))
    status: str = Column(String(50))
    username: str = Column(String(50))
    creation_time: datetime = Column(DateTime)

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, db_name={self.db_name!r}, status={self.status!r}, username={self.username!r}, "
                f"creation_time={self.creation_time!r})")



