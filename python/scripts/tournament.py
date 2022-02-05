from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_tournament(tTitle):
    """
    Function for tournament creation
    """

    session = open_session()

    tournament=Tournament(title=tTitle)
    session.add(tournament)

    session.commit()

    session.close()