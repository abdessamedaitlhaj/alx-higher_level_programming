#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
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

    new_city = City()
    new_state = State()
    new_city.name = "San Francisco"
    new_state.name = "California"
    new_state.cities.append(new_city)
    session.add(new_city)
    session.add(new_state)
    session.commit()
    session.close()
    engine.dispose()
