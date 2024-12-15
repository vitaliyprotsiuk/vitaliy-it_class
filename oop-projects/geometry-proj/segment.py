from figure import Figure
import math


class Segment(Figure):
    __pointA = None
    __pointB = None

    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    def lenght(self, pointA, pointB):
        x1 = pointA.getX()
        y1 = pointA.getY()
        x2 = pointB.getX()
        y2 = pointB.getY()

        lenght = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return round(lenght, 2)
    
    def perimeter(self):
        return 10
    
    def __str__(self):
        
        segment = f"A{'_'*math.floor(self.lenght(self.__pointA, self.__pointB))}B"
        
        return segment