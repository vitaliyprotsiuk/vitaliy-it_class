class Tournament:
    __games = []
    __teams = []

    def __init__(self, games, teams):
        self.__games = []
        self.__teams = teams
        for game in games:
            self.add_game(game)
        self.sort_teams()

    def sort_teams(self):
        for i in range(0, len(self.__teams)):
            for j in range(i, len(self.__teams)):
                if self.__teams[i].get_points() < self.__teams[j].get_points():
                    temp = self.__teams[i]
                    self.__teams[i] = self.__teams[j]
                    self.__teams[j] = temp

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
        print(f"Team Name        | W | D | L | P")
        for team in self.__teams:
            print(f"{team} {str(team.get_wins()) + ' |'} {str(team.get_draws()) + ' |'} {str(team.get_loses()) + ' |'} {str(team.get_points()) + ''}")