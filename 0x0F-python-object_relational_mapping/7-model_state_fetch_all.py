#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

db_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(db_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(State).order_by(State.id).all()
for q in query:
    print("{}: {}".format(q.id, q.name))
session.close()
