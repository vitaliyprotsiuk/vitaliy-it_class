class CarShop:
    __cars = []

    def __init__(self, cars):
        self.__cars = cars

    def printAllCars(self):
        for car in self.__cars:
            car.print()

    def getTopSpeedCar(self):
        if self.__cars == 0:
            return
        

        top_speed = self.__cars[0].getMaxSpeed()
        top_speed_car = self.__cars[0]
        for car in self.__cars:
            if car.getMaxSpeed() > top_speed:
                top_speed = car.getMaxSpeed()
                top_speed_car = car

        return top_speed_car
    
    def findCars(self, min_year, max_year, min_price, max_price):
        foundCars = []

        for car in self.__cars:
            if self._satisfyPrice(car, min_price, max_price) and self._satisfyYear(car, min_year, max_year):
                foundCars.append(car)

        return foundCars
    
    def _satisfyPrice(self, car, min_price, max_price):
        if car.getPrice() >= min_price and car.getPrice() <= max_price:
            return True
        
        return False
    
    def _satisfyYear(self, car, min_year, max_year):
        if car.getYear() >= min_year and car.getYear() <= max_year:
            return True
        
        return False