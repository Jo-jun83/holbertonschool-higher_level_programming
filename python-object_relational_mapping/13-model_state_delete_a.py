#!/usr/bin/python3
"""
This module connects to a MySQL database using SQLAlchemy
and deletes all State objects with a name containing the
letter a from the database .
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user,
            password,
            database
        )
    )

    session = Session(engine)
    states = session.query(State).filter(
        State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
        session.commit()
