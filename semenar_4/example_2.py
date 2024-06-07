# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


# 1 способ
# def fix_unicode(text: str) -> list[int]:
#     code_list = []
#     for char in set(text):
#         code_list.append(ord(char))
#     return sorted(code_list, reverse = True)
#
#
#
# string = input("Введите текст: ")
# print(fix_unicode(string))

# 2 способ
def f(x1: str) -> list[int]:
    print(sorted([ord(char) for char in set(x1)], reverse=True))

string = input("Введите текст: ")
f(string)

