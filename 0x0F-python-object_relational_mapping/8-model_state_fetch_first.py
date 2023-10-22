#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(
                    sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()

    if result is None:
        print("Nothing")
    print('{}: {}'.format(result.id, result.name))
