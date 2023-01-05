from Config.database import Base
from sqlalchemy import (
    String,Integer,Float,Column
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(
             Integer,
             primary_key=True,
             autoincrement=True
    )
    title = Column(
            String 
    )
    overview = Column(
               String
    )
    year = Column(
           Integer
    )
    rating = Column(
             Float
    )
    category = Column(
               String
    )