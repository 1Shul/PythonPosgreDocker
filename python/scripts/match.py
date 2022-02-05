from scripts.database import open_session
from scripts.models import Tournament, Teams, Matches

def create_match():
    session = open_session()

    #user=session.query(Tournament).all()
    #print(user)
    teamA=session.query(Teams).filter_by(name=input("Ingrese el nombre del primer equipo")).first()
    teamB=session.query(Teams).filter_by(name=input("Ingrese el nombre del segundo equipo")).first()

    golesA = int(input("Ingrese la cantidad de goles del primer equipo"))
    golesB = int(input("Ingrese la cantidad de goles del segundo equipo"))

    match=Matches(idLocalTeam=teamA.id, idVisitorTeam=teamB.id, goalLocalTeam=golesA, goalVisitorTeam=golesB)
    session.add(match)

    #print('flush')

    session.commit()

    #our_tournament = session.query(Tournament).filter_by(title='Ptmr').first()

    session.close()