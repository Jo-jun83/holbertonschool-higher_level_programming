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
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user,
            password,
            database
        )
    )

    session = Session(engine)
    results = session.query(State).filter(
        State.name == state
    ).order_by(State.id).first()
    print("Not found" if not results else results.id)
