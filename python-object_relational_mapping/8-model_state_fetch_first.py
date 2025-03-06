#!/usr/bin/python3
"""
This module connects to a MySQL database using SQLAlchemy
and retrieves the first
State object from the database.
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
    results = session.query(State).order_by(State.id).first()
    if not results:
        print("Nothing")
    print("{}: {}".format(results.id, results.name))
