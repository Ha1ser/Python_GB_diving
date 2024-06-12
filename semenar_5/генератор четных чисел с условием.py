# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# решение через функцию
# def even(limit):
#     for number in range(0, limit + 1, 2):
#         if number % 10 + number // 10 != 8:
#             yield number
#
# print(list(even(100)))

even_num = (number for number in range(0, 100 + 1, 2) if number % 10 + number // 10 != 8)
print(*even_num)


