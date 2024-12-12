class Car:
    __name = ""
    __price = 0
    __year = 0
    __max_speed = 0

    def __init__(self, name, price, year, max_speed):
        self.__name = name
        self.__price = price
        self.__year = year
        self.__max_speed = max_speed
    
    def getPrice(self):
        return self.__price
    
    def getName(self):
        return self.__name
    
    def getMaxSpeed(self):
        return self.__max_speed
    
    def getYear(self):
        return self.__year
    
    def drive(self):
        return f"Wroom! I am {self.__name}"
    
    def printMaxSpeedCar(self):
        return f"Car that has the fastest speed is: {self.__name}"
    
    def print(self, car):
        print(f"Name: {self.__name}. Year: {self.__name}. Speed: {self.__max_speed}. Price: {self.__price}")