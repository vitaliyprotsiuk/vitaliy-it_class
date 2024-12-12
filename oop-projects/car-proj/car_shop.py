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