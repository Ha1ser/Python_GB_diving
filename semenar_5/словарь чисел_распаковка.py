# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

# 1 способ - мой код
# numbers = input("Введите 4 и более целых чисел, разделённых символом “/”: ").split("/")
# slov = {}
# c = list()
# for i in range(len(numbers)):
#     a = int(numbers[0])
#     key1 = int(numbers[1])
#     key2 = int(numbers[2])
#     if numbers[i] != a and numbers[i] != key1 and numbers[i] != key2:
#         c.append(int(numbers[i]))
#     slov[key1] = a
#     slov[key2] = tuple(c)
#
# print(slov)

# 2 способ
# numbers = input("Введите 4 и более целых чисел, разделённых символом “/”: ").split("/")
# num1, num2, num3, *num4 = numbers
# slove = {}
# slove[int(num2)] = int(num1)
# slove[int(num3)] = tuple(map(int, num4))
# print(slove)

# 3 способ
num1, num2, num3, *list_nums = input("Введите 4 и более целых чисел, разделённых символом “/”: ").split("/")
dict_1 = {
    int(num2): int(num1),
    int(num3): tuple(map(int, list_nums))
}
print(f"{dict_1 = }")