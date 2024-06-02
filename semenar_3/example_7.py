# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

# реш 1 count
# t = input("введите текст: ")
# result = {}
# for char in set(t):
#     result[char] = t.count(char)
#
# print(result)

# t = input("введите текст: ")
# result = {}
# for char in t:
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1
# print(result)

# 3
t = input("введите текст: ")
result = {}
for char in t:
    result[char] = result.get(char, 0) + 1

print(result)
