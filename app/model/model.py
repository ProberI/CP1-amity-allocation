from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Employees(Base):
    __tablename__ = 'Amity_employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Emp_Id = Column(String(250))
    Person_name = Column(String(350))
    role = Column(String(250))
    unallocated = Column(String(100))


class All_rooms(Base):
    __tablename__ = "Amity_rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Room_name = Column(String(250))
    Room_type = Column(String(250))
    Occupants = Column(String(500), nullable=True)


def create_db(db_name):
    engine = create_engine('sqlite:///model/' + db_name + '.db')
    Base.metadata.create_all(engine)
