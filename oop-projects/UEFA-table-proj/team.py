class Team:
    __id = 0
    __name = ""
    __wins = 0
    __loses = 0
    __draws = 0    
    __games = []

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    def add_game(self, game):
        self.__games.append(game)

        home_score = game.get_home_team_score()
        away_score = game.get_away_team_score()

        if home_score == away_score:
            self.__draws += 1
        elif self == game.get_home_team() and home_score > away_score:
            self.__wins += 1
        elif self == game.get_away_team() and home_score < away_score:
            self.__wins += 1
        else:
            self.__loses += 1

    def get_points(self):   
        return self.__wins * 3 + self.__draws
    
    def get_wins(self):
        return self.__wins
    
    def get_draws(self):
        return self.__draws
    
    def get_loses(self):
        return self.__loses
    
    def get_id(self):
        return self.__id

    def __str__(self):
        return self.__name
    
    def __eq__(self, value):
        return self.__name == value