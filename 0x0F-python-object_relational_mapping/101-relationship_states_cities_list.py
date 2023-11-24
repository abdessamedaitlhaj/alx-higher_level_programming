#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects
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

    states = session.query(State).order_by(State.id)
    for st in states:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("   {}: {}".format(ct.id, ct.name))
    session.close()
    engine.dispose()
