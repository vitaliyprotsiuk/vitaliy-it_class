from segment import Segment
from figure import Figure
from point import Point

class RectangleAndSquare(Figure):
    __pointA = None
    __pointC = None

    def __init__(self, pointA, pointC):
        self.__pointA = pointA
        self.__pointC = pointC

        self.__pointB = Point(self.__pointA.get_x(), self.__pointC.get_y())
        self.__pointD = Point(self.__pointC.get_x(), self.__pointA.get_y())

    # creating sides
    def sides(self):
        side_a = Segment(self.__pointA, self.__pointB)
        side_b = Segment(self.__pointB, self.__pointC)
        side_c = Segment(self.__pointC, self.__pointD)
        side_d = Segment(self.__pointD, self.__pointA)

        return side_a, side_b, side_c, side_d

    # rectangle or square
    def checking(self):
        side_a = self.sides()[0]
        side_b = self.sides()[1]
        side_c = self.sides()[2]
        side_d = self.sides()[3]

        if side_a.length() == side_b.length() and side_b.length() == side_c.length() and side_c.length() == side_d.length():
            return True
        else:
            return False
        
    def perimeter(self):
        side_a = self.sides()[0]
        side_b = self.sides()[1]
        side_c = self.sides()[2]
        side_d = self.sides()[3]
        
        perimeter = side_a.length() + side_b.length() + side_c.length() + side_d.length()

        return perimeter
    
    def square(self):
        side_a = self.sides()[0]
        side_b = self.sides()[1]

        square = side_a.length() * side_b.length()

        return square
        
    def __str__(self):
        if self.checking() == True:
            return f"Квадрат побудований"
        else:
            return "Прямокутник побудований"