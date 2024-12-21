class Tournament:
    __games = []
    __teams = []

    def __init__(self, games, teams):
        self.__games = []
        self.__teams = teams
        for game in games:
            self.add_game(game)


    def _find_team(self, team):
        for item in self.__teams:
            if item == team:
                return team

    def add_game(self, game):
        self.__games.append(game)

        homeTeam = self._find_team(game.get_home_team())
        homeTeam.add_game(game)

        awayTeam = self._find_team(game.get_away_team())
        awayTeam.add_game(game)

    def print_table(self):
        print(f"Team Name       | W | D | L | P")
        for team in self.__teams:
            print(f"{team} {team.get_wins()} {team.get_draws()} {team.get_loses()} {team.get_points()}")
