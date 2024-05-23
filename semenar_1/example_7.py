# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print



# решение 1
# num_1 = 1
# num_2 = 999
#
# n = int(input('Введите число от 1 - 999: '))
#
# if n > num_2 or n < num_1:
#     res = "введите новое число"
# else:
#     if n // 100 != 0:
#         a_1 = str(n // 100)
#         a_2 = str((n //10) % 10)
#         a_3 = str(n % 10)
#         res = f"Введенно трехзначное число, зеркальное отражение трехзначного числа — {a_3 + a_2 + a_1}"
#     elif n // 10 != 0:
#         res = f"Введенно двухзначное число, произведение двухзначного числа — {(n // 10) * (n % 10)}"
#     else:
#         res = f"введина цифра, квадрат n — {n ** 2}"
#
#
# print(res)

# решение 2
low_limit = 0
up_limit = 1000
one = 1
ten = 10
hungred = 100
square = 2

num = low_limit
while num <= low_limit or num >= up_limit:
    num = int(input(f"введите число от {low_limit + one} до {up_limit - one}: "))
else:
    if num < ten:
        result = f"число {num} - цифра. Ее квадрат = {num ** square}"
    elif num < hungred:
        prod = (num // ten) * (num % ten)
        result = f"число {num} - двухзначное. произведение = {prod}"
    else:
        mirror = (num % ten * hungred) + ((num // ten % ten) * ten) + (num // hungred)
        result = f"число {num} - трехзначное. зеркальное число = {mirror}"

print(result)


