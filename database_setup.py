import os
import sys
from sqlalchemy import Column,DateTime,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine
import datetime


Base = declarative_base()

class Alldata(Base):
    __tablename__='all_data'
    headline = Column(String(200),nullable=False)
    source = Column(String(30), nullable=False)
    url = Column( String(300))
    category = Column(String(30),nullable=False)
    key = Column(Integer,primary_key=True)
    uploaded = Column(DateTime, default=datetime.date.today())
    actual = Column(String(30))
    


engine = create_engine('sqlite:///newsdata.db')
Base.metadata.create_all(engine)
