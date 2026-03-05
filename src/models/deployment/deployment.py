from sqlalchemy import ForeignKey
from sqlalchemy import String, UUID, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Deployment(Base):

    __tablename__ = 'deployments'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    db_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[str]
    username: Mapped[str]
    creation_time: Mapped[DateTime]
