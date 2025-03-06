#!/usr/bin/python3
"""
This module connects to a MySQL database using SQLAlchemy
and lists all State objects that contain the letter a from
the database.
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )

    session = Session(engine)
    results = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()
    for result in results:
        print("{}: {}".format(result.id, result.name))
