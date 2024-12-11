import math

class Circle:
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    def calculateLenght(self, radius):
        lenght = 2*3.14*radius

        return round(lenght, 1)
    
    def calculateArea(self, radius):
        area = radius**2*3.14
        
        return round(area, 1)