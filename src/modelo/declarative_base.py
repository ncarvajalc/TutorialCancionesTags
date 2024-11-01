from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///aplicacion.sqlite")
engine_copy = engine

print(engine=engine_copy)

Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
