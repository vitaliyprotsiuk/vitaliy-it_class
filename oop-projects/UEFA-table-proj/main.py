from scripts.team import Team
from scripts.game import Game
from data.config import *
from scripts.window import Window


def read_teams():
    file_teams = open(TEAMS_PATH)
    teams = []
    while True:
        team_line = file_teams.readline()
        if team_line == '':
            break

        props = team_line.split(' ')
        team = Team(int(props[0]), props[1])
        teams.append(team)
    return teams


def find_team_by_id(teams, team_id):
    for team in teams:
        if team.get_id() == team_id:
            return team


def read_games(teams):
    file_games = open(GAMES_PATH)
    games = []
    while True:
        game_line = file_games.readline()
        if game_line == '':
            break

        props = game_line.split(' ')
        id_home_team = int(props[1])
        id_away_team = int(props[2])
        home_team_score = int(props[3])
        away_team_score = int(props[4])

        game = Game(props[0], find_team_by_id(teams, id_home_team), find_team_by_id(teams, id_away_team), home_team_score, away_team_score)
        games.append(game)


    return games


teams = read_teams()
games = read_games(teams)


window = Window(teams, games)
window.start_window()


"""intcmd = IntCMD(games, teams)
intcmd.cheking()"""