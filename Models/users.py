from sqlalchemy import (
    Column,String,Integer
)

from Config.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(
         Integer,
         primary_key=True,
         autoincrement=True
    )
    email = Column(
        String,
        nullable=False,
        unique=True
    )
    passwd = Column(
        String,
        nullable = False
    )