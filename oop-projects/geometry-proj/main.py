from circle import Circle
from rectangle import Rectangle

action = int(input("1. Обчислити периметр прямокутника\n2. Обчислити площу прямокутника\n3. Обчислити довжину кола\n4. Обчислити площу кола\nВведіть дію, яку хочете виконати: "))

if action == 1:
    a = int(input("Введіть сторону a: "))
    b = int(input("Введіть сторону b: "))

    rectangle = Rectangle(a, b)

    print(rectangle.calculatePerimeter(a, b))

if action == 2:
    a = int(input("Введіть сторону a: "))
    b = int(input("Введіть сторону b: "))

    rectangle = Rectangle(a, b)

    print(rectangle.calculateArea(a, b))

if action == 3:
    radius = int(input("Введіть радіус кола: "))

    circle = Circle(radius)

    print(circle.calculateLenght(radius))

if action == 4:
    radius = int(input("Введіть радіус кола: "))

    circle = Circle(radius)

    print(circle.calculateArea(radius))