# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scripts.database import creacion
from scripts.tournament import create_tournament
from scripts.team import create_team
from scripts.match import create_match
from scripts.export import export_data, export_teams


"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint."""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    APP START
    """
    # print_hi('PyCharm')
    creacion()
    print('creado')
    a = int(input("Ingrese un numero:"))
    if 0 == a:
        create_tournament(input("Ingrese nombre del torneo:"))
    if 1 == a:
        create_team(input("Ingrese nombre del torneo:"))
    if 2 == a:
        create_match()
    if 3 == a:
        export_data()
        export_teams()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
