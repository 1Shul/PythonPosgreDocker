from scripts.database import db_create
from scripts.tournament import create_tournament
from scripts.team import create_team
from scripts.match import create_match
from scripts.export import export_data, export_teams, export_matches

if __name__ == '__main__':
    """
    APP START
    """
    db_create()

    print("0. Create tournament")
    print("1. Create team")
    print("2. Register match result")
    print("3. Export data to CSV")
    
    a = int(input("Enter a number:"))
    if 0 == a:
        create_tournament(input("Insert tournament name: "))
    if 1 == a:
        create_team(input("Insert team name: "))
    if 2 == a:
        create_match()
    if 3 == a:
        export_data()
        export_teams()
        export_matches()