from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_team(tName):
    """
    Function for team creation
    """
    session = open_session()

    team=Teams(name=tName)
    session.add(team)

    session.commit()

    session.close()