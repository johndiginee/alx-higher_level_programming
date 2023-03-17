#!/usr/bin/python3
"""
Script defines a City class
to work with MySQLAlchemy ORM.
"""

from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
