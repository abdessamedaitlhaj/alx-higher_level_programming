#!/usr/bin/python3
"""
Script that lists all City objects from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)
    for st in states:
        for ct in st.cities:
            print("{}: {} -> {}".format(ct.id, ct.name, st.name))
    session.close()
    engine.dispose()
