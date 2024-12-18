from figure import Figure
import math

class Triangle(Figure):
    __segment1 = None
    __segment2 = None
    __segment3 = None

    def __init__(self, segment1, segment2, segment3):
        self.__segment1 = segment1
        self.__segment2 = segment2
        self.__segment3 = segment3

    def get_length(self):
        # getting length of segments
        lenseg1 = self.__segment1.length()
        lenseg2 = self.__segment2.length()
        lenseg3 = self.__segment3.length()

        lenghtsarray = [lenseg1, lenseg2, lenseg3]

        return lenghtsarray
    
    def checking(self):
        lengthsarray = self.get_length()

        # getting 2 minimal items
        min1 = min(lengthsarray)
        lengthsarray.pop(lengthsarray.index(min1))   

        min2 = min(lengthsarray)
        lengthsarray.pop(lengthsarray.index(min2))

        # checking 
        if min1 + min2 >= lengthsarray[0]:
            return True
        else:
            return False
        
    def __str__(self):
        if self.checking() == True:
            return f'Трикутник ABC може існувати з відрізків: \n{self.__segment1}\n{self.__segment2}\n{self.__segment3}'
        else: 
            return 'Трикутник ABC не може бути побудований з цих відрізків!'
        
    def square(self):
        p = self.perimeter() / 2

        # according to the formula p(p-a)(p-b)(p-c)
        if self.checking() == True:
            square = int(math.sqrt(p*(p - self.__segment1.length())*(p - self.__segment2.length())*(p - self.__segment3.length())))
            return square
        else: 
            return 0

    def perimeter(self):
        len1 = self.__segment1.length()
        len2 = self.__segment2.length()
        len3 = self.__segment3.length()


        if self.checking() == True:
            perimeter = len1 + len2 + len3

            return perimeter
        else: 
            return 0