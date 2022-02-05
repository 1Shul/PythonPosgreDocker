from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_match():

    """
    Function for match result registration
    """

    session = open_session()

    teamA=session.query(Teams).filter_by(name=input("Enter the first team name: ")).first()
    teamB=session.query(Teams).filter_by(name=input("Enter the second team name: ")).first()

    golesA = int(input("Insert the goal quantity of the first team: "))
    golesB = int(input("Insert the goal quantity of the second team: "))

    match=Matches(idLocalTeam=teamA.id, idVisitorTeam=teamB.id, goalLocalTeam=golesA, goalVisitorTeam=golesB)
    session.add(match)

    session.commit()

    session.close()