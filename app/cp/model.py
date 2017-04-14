import os
import sys
import time
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Employees(Base):
    __tablename__ = 'Amity_employees'
    Emp_Id = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    role = Column(String(250))


class Rooms(Base):
    __tablename__ = "Amity_rooms"
    Room_name = Column(String(250))
    Room_type = Column(String(250))


engine = create_engine("sqlite:///tasklist.db")

Base.metadata.create_all(engine)
