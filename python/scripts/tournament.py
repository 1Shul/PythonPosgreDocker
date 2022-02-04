from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_tournament(tTitle):
    session = open_session()

    # user=session.query(Tournament).all()
    # print(user)

    tournament=Tournament(title=tTitle)
    session.add(tournament)

    # print('flush')

    session.commit()

    # tour_tournament = session.query(Tournament).filter_by(title='Ptmr').first()

    session.close()