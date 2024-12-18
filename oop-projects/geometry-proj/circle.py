from figure import Figure

class Circle(Figure):
    __point = None
    __radius = 0

    def __init__(self, point, radius):
        self.__point = point
        self.__radius = radius

    def perimeter(self):
        p = 3.14

        length = 2*p*self.__radius
        
        return length

    def __str__(self):
        return f"Коло з центом в точці - {self.__point} і радіусом = {self.__radius}"