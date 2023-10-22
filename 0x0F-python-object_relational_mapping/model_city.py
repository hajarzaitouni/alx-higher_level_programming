#!/usr/bin/python3
"""
Define City class
that inherits from Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    create City class for MySQL database

    Attributes:
        __tablename__ (str): MySQL table's name to store cities.
        id (int): city's id.
        name (str): city's name.
        state_id (int): city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
