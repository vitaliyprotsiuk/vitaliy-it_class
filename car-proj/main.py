from car import Car
from car_filter import CarFilter
from car_shop import CarShop

nazar_dream_car = Car("Porsche Taycan", 300000, 2024, 280)
vitalik_dream_car = Car("Tesla Plaid", 200000, 2022, 282)
mattew_dream_car = Car("Toyota Land Cruiser 200", 100000, 2024, 180)

it_club_dream_cars = [nazar_dream_car, vitalik_dream_car, mattew_dream_car]

shop = CarShop(it_club_dream_cars)

filter = CarFilter(1990, 2026, 0, 1000000) # args: min. year, max. year, min. price, max. price

# shop.printAllCars()

for i in it_club_dream_cars:
    if filter.acceptCar(i, 0, 100001, 1996, 2900) == True:
        required_car = Car.drive(i)
        print(required_car)