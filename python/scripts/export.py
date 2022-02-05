import csv
from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def export_data():
    session=open_session()
    # tournaments_id=[]
    # tournaments_name=[]
    tournaments=[]
    for i in session.query(Tournament).all():
        tournament=[]
        tournament.append(i.id)
        tournament.append(i.title)
        tournaments.append(tournament)
        # tournaments_id.append(i.id)
        # tournaments_name.append(i.title)
    # print(list(session.query(Tournament).all()))

    # tournament=[]
    # tournament.append(tournaments_id)
    # tournament.append(tournaments_name)

    session.close()

    print(tournaments)

    with open('export.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerows(tournaments)

def export_teams():
    session=open_session()

    teams=[]

    for i in session.query(Teams).all():
        team=[]
        team.append(i.id)
        team.append(i.name)
        teams.append(team)

    session.close()

    with open('export_teams.csv', 'w', newline='') as file:
        wr = csv.writer(file,quoting=csv.QUOTE_ALL)
        wr.writerows(teams)