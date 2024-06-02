# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# 1 способ
# import math
# import decimal
#
# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)
#
# d = decimal.Decimal(input('введите диаметр: '))
# s = PI * (d / 2) ** 2
# l = PI * d
# print(f"{s=}")
# print(f"{l=}")


import math
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

d = decimal.Decimal(input('введите диаметр: '))
while d > 1000:
    print("Введенно число вне диапазона, больше 1000")
    d = decimal.Decimal(input('введите диаметр: '))

s = PI * (d / 2) ** 2
l = PI * d
print(f"{s=}")
print(f"{l=}")

