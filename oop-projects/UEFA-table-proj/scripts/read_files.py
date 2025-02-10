from data.config import TEAMS_PATH, GAMES_PATH
from scripts.game import Game
from scripts.team import Team

def read_games(teams: list):
    games = []
    with open(GAMES_PATH, 'r') as games_file:
        while True:
            line = games_file.readline()
            if line == '':
                break

            array = line.split(' ')
            game = Game(find_name_by_id(teams, int(array[1])), find_name_by_id(teams, int(array[2])), int(array[3]), int(array[4]))
            games.append(game)
        
        return games


def read_teams():
    teams = []
    with open(TEAMS_PATH, 'r') as teams_file:
        while True:
            line = teams_file.readline()
            if line == '':
                break

            array = line.split(' ')
            team = Team(int(array[0]), array[1])
            teams.append(team)

        return teams


# additional functions
def find_name_by_id(teams: list, id: int):
    for team in teams:
        if team.get_id() == id:
            return team