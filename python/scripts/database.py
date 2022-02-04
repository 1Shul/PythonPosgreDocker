from scripts.config import DATABASE_URI
from scripts.models import Base, Tournament, Teams, Matches
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)

def creacion():

    Base.metadata.create_all(engine)
    #print(Base.metadata.tables)

def open_session():
    Session = sessionmaker(bind=engine)
    return Session()




