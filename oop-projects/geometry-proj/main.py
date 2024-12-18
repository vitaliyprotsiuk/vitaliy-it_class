from circle import Circle
from triangle import Triangle
from point import Point
from segment import Segment
from rectangle_and_square import RectangleAndSquare

# figures
pointA1 = Point(2, 1)
pointB1 = Point(5, 4)
pointA2 = Point(0, 0)
pointB2 = Point(5, 5)
pointA3 = Point(0, 0)
pointB3 = Point(2, 2)
segment1 = Segment(pointA1, pointB1)
segment2 = Segment(pointA2, pointB2)
segment3 = Segment(pointA3, pointB3)
triangle = Triangle(segment1, segment2, segment3)
circle = Circle(pointA1, 2) # center point, radius

rectangle = RectangleAndSquare(pointA1, pointB1)



figures = [rectangle]

for figure in figures:
    peremiter = figure.perimeter()
    square = figure.square()
    print(f"{figure}, P={peremiter}, Square={square}")