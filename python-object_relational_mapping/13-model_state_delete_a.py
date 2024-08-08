#!/usr/bin/python3
"""deletes data from database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(State).filter(State.name.like('%a%'))
        count = 0
        for row in result:
            session.delete(row)
            count += 1
        session.commit()
        print("Deleted {} rows".format(count))
    except Exception as e:
        print("Error: {}".format(e))
        session.rollback()
    finally:
        session.close()
