from figure import Figure
import math


class Segment(Figure):
    __pointA = None
    __pointB = None

    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    def square(self):
        return self.length()

    def length(self):
        x1 = self.__pointA.get_x()
        y1 = self.__pointA.get_y()
        x2 = self.__pointB.get_x()
        y2 = self.__pointB.get_y()

        lenght = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        return int(lenght)
    
    def perimeter(self):
        perimeter = self.length()

        return perimeter
    
    def __str__(self):
        segment = f"A{'_'*math.floor(self.length())}B"
        
        return segment