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

    session.add(Tournament(title="Qatar"))
    session.add(Teams(name="Peru"))
    session.add(Teams(name="Portugal"))
    session.add(Matches(idLocalTeam=1, idVisitorTeam=2, goalLocalTeam=2, goalVisitorTeam=1))

    session.commit()

    session.close()



def open_session():

    """
    Function for SQLAlchemy session
    """

    Session = sessionmaker(bind=engine)
    return Session()




