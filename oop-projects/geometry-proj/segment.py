from figure import Figure

class Segment(Figure):
    __pointA = None
    __pointB = None

    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    def perimeter(self):
        return 10
    
    def __str__(self):
        return "A"