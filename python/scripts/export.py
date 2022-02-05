import csv
from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def export_data():

    """
    Function for exporting tournaments data to CSV
    """

    session=open_session()

    tournaments = []
    
    for i in session.query(Tournament).all():
        tournament = []
        tournament.append(i.id)
        tournament.append(i.title)
        tournaments.append(tournament)

    session.close()

    print(tournaments)

    with open ('export.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerows(tournaments)

def export_teams():

    """
    Functions to export teams data to CSV
    """

    session=open_session()

    teams = []

    for i in session.query(Teams).all():
        team = []
        team.append(i.id)
        team.append(i.name)
        teams.append(team)

    session.close()

    with open ('export_teams.csv', 'w', newline='') as file:
        wr = csv.writer(file,quoting=csv.QUOTE_ALL)
        wr.writerows(teams)

def export_matches():

    """
    Function to export matches result data to CSV
    """

    session=open_session()

    matches = []

    for i in session.query(Matches).all():
        match = []
        match.append(i.id)
        match.append(session.query(Teams).filter_by(id=i.idLocalTeam).first())
        match.append(i.goalLocalTeam)
        match.append(session.query(Teams).filter_by(id=i.idVisitorTeam).first())
        match.append(i.goalVisitorTeam)

    session.close()

    with open ('export_matches.csv', 'w', newline='') as file:
        wr = csv.writer(file,quoting=csv.QUOTE_ALL)
        wr.writerows(matches)