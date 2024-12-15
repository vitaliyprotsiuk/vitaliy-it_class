from figure import Figure


class Point(Figure):
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y