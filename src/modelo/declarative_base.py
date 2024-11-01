from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///aplicacion.sqlite")


def check_value(value):
    if value == None:
        print("Engine is None")
    else:
        print("Engine is not None")


check_value(engine)

Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
