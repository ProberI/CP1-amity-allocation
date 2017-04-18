import os

import sys

import time

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Employees(Base):
    __tablename__ = 'Amity_employees'
    Emp_Id = Column(String(250), primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    role = Column(String(250))


class _Rooms(Base):
    __tablename__ = "Amity_rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Room_name = Column(String(250))
    Room_type = Column(String(250))


def create_db(db_name):
    # db_name = 'amity'
    engine = create_engine('sqlite:///' + db_name + '.db')
    Base.metadata.create_all(engine)


# create_db('amity')
