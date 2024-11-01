from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///aplicacion.sqlite")


def append_to_correct_urls(value, list_of_urls=[]):
    list_of_urls.append(value)
    return list_of_urls


Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
