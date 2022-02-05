from scripts.config import DATABASE_URI
from scripts.models import Base, Tournament, Teams, Matches
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)

def db_create():

    """
    Function for database creation
    """

    Base.metadata.create_all(engine)
    #print(Base.metadata.tables)

    session=open_session()

    session.add(Tournament('Qatar'))
    session.add(Teams('Peru'))
    session.add(Teams('Portugal'))
    session.add(Matches(1,2,2,1))



def open_session():

    """
    Function for SQLAlchemy session
    """

    Session = sessionmaker(bind=engine)
    return Session()




