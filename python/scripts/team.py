from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_team(tName):
    session = open_session()

    #user=session.query(Tournament).all()
    #print(user)

    team=Teams(name=tName)
    session.add(team)

    #print('flush')

    session.commit()

    #our_tournament = session.query(Tournament).filter_by(title='Ptmr').first()

    session.close()