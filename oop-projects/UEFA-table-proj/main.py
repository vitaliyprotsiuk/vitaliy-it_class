from team import Team
from table import Table

liverpool = Team('Ліверпуль', 6, 6, 0, 0, 13, 1, 18, '✅ ✅ ✅ ✅ ✅')
barcelona = Team('Барселона', 6, 5, 0, 1, 21, 7, 15, '✅ ✅ ✅ ✅ ✅')
arsenal = Team('Арсенал  ', 6, 4, 1, 1, 11, 2, 13, '✅ ❌ ✅ ✅ ✅')

array_teams = [liverpool, barcelona, arsenal]

table = Table(array_teams)

table.draw_table()