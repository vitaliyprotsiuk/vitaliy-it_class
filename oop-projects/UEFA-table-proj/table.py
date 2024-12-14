from team import Team

class Table():
    _teams = None

    def __init__(self, teams):
        self._teams = teams

    def draw_table(self):
        print('-----------------------------UEFA Table-----------------------------')
        print()
        print()
        print()
        print("Клуб           | І | В | Н | П | МЗ | МП | РМ | О |     Останні 5   ")
        print('--------------------------------------------------------------------')
        
        for i in self._teams:
            print(i)