# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

space = " "
star = "*"

rows = int(input(f"Сколько рядов у елки: "))
spaces = rows - 1
stars = 1

for _ in range(rows):
    print((spaces * space) + (stars * star))
    stars += 2
    spaces -= 1

