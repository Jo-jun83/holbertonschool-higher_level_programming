#!/usr/bin/python3
"""
This module defines a SQLAlchemy ORM model for the 'states' table.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    State class that maps to the 'states' table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
