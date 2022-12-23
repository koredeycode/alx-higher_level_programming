#!/usr/bin/python3
"""Prints the first State object fom the database"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = State(name='California')
    st.cities = [City(name='San Francisco')]
    session.add(st)
    session.commit()
    session.close()
