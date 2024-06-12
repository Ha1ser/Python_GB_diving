# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# прога с помощью функции
# def prog(limit):
#     for res in range(1, limit + 1):
#         if res % 3 == 0 and res % 5 == 0:
#             print("FizzBuzz")
#         elif res % 5 == 0:
#             print("Buzz")
#         elif res % 3 == 0:
#             print("Fizz")
#         else:
#             print(res)
#
# prog(100)



# решение с семенара
LOW_LIMIT = 1
UP_LIMIT = 101
DIV1 = 3
DIV2 = 5
# for num in range(LOW_LIMIT,UP_LIMIT):
# if num % (DIV1 * DIV2) == 0:
# print("FizzBuzz")
# elif num % DIV1 == 0:
# print("Fizz")
# elif num % DIV2 == 0:
# print("Buzz")
# else:
# print(num)

print(*(
    "FizzBuzz" if num % (DIV1 * DIV2) == 0 else
    "Fizz" if num % DIV1 == 0 else
    "Buzz" if num % DIV2 == 0 else num
    for num in range(LOW_LIMIT,UP_LIMIT)
), sep="\n")



