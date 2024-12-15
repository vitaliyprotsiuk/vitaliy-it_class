from point import Point
from segment import Segment

pointA = Point(0, 0)
pointB = Point(10, 10)
segment1 = Segment(pointA, pointB)

figures = [pointA, pointB, segment1]

print(f"Довжина відрізку = {segment1.lenght(pointA, pointB)}")

for figure in figures:
    peremiter = figure.perimeter()
    print(f"{figure}, P={peremiter}")