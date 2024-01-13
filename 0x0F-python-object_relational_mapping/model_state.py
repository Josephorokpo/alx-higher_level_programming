#!/usr/bin/python3
"""
Module containing the class definition of a State and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    Class representing the State table.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
