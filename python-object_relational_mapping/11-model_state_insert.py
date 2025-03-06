#!/usr/bin/python3
"""
This module connects to a MySQL database using SQLAlchemy
and adds the State object “Louisiana” to the database.
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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
