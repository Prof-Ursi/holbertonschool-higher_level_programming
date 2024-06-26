#!/usr/bin/python3
"""
Script that adds the 'State' object “Louisiana”
to the database 'hbtn_0e_6_usa'.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    session.commit()
    louisiana = session.query(State).filter(State.name == "Louisiana").first()
    print(louisiana.id)
    session.close()
