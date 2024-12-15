from point import Point
from segment import Segment

pointA = Point(5, 10)
pointB = Point(5, 13)
segment1 = Segment(pointA, pointB)

figures = [pointA, pointB, segment1]

for figure in figures:
    peremiter = figure.perimeter()
    print(f"{figure}, P={peremiter}")