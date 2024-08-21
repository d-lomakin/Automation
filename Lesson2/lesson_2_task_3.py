import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = float(input("Введите длину стороны квадрата: "))

print(f"Площадь квадрата: {square(side_length)}")
