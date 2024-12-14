class Team:
    _name = None
    _games = 0
    _wins = 0
    _loses = 0
    _draws = 0
    _goals = 0
    _skiped_balls = 0
    _balls_diference = 0
    _score = 0
    _last_five = None

    def __init__(self, name, games, wins, loses, draws, goals, skipped_balls, score, last_five):
        self._name = name
        self._games = games
        self._wins = wins
        self._loses = loses
        self._draws = draws
        self._goals = goals
        self._skiped_balls = skipped_balls
        self._balls_diference = goals - skipped_balls
        if self._balls_diference < 10:
            self._balls_diference = str(self._balls_diference)
            self._balls_diference = f' {self._balls_diference}'
        else: self._balls_diference = goals - skipped_balls
        self._score = score
        self._last_five = last_five
        
    def __str__(self):
        return f'{self._name}      | {self._games} | {self._wins} | {self._loses} | {self._draws} | {self._goals} | {self._skiped_balls} | {self._balls_diference} | {self._score} | {self._last_five}'