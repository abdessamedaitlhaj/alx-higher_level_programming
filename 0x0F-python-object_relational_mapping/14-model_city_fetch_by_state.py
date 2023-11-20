#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State.name, City.id, City.name).filter(State.id == City.state_id).all()
    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
    engine.dispose()
