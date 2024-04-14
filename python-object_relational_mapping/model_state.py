#!/usr/bin/python3
'''
    Using the SQL Alchemy in defining a database
    states Database table
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    '''A class defination of a table in the sql'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
