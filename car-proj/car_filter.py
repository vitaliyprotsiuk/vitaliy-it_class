class CarFilter:
    __min_year = 0
    __max_year = 0
    __min_price = 0
    __max_price = 0

    def __init__(self, min_price, max_price, min_year, max_year):
        self.__min_price = min_price
        self.__max_price = max_price
        self.__min_year = min_year
        self.__max_year = max_year

    def acceptCar(self, car, min_price, max_price, min_year, max_year):
        if self._satisfyPrice(car, min_price, max_price) and self._satisfyYear(car, min_year, max_year):
            return True
        
        return False
    
    def _satisfyPrice(self, car, min_price, max_price):
        if car.getPrice() >= min_price and car.getPrice() <= max_price:
            return True
        
        return False
    
    def _satisfyYear(self, car, min_year, max_year):
        if car.getYear() >= min_year and car.getYear() <= max_year:
            return True
        
        return False

    def print_4():
        print(4)
