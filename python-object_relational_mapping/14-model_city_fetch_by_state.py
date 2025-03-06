#!/usr/bin/python3
"""
This module lists all City objects from the database.
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
