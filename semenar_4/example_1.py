# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# 1 способ - мой код
# g = "qwerty asdf zxcv fdslkfj fdsjkfkds guwjnaf bnkjakfnw grwkjnoif glwkn igew nigew ngiwen gnw jngwkejgnrk jgbnwkgkejg"
#
# def strok(x1):
#     res = x1.split()
#     res = sorted(res)
#     max_lens = 0
#     for item in res:
#         lens = len(item)
#         if max_lens < lens:
#             max_lens = lens
#
#     for i, j in enumerate(res, 1):
#         print(f"{i:>2}. {j:>{max_lens}}")
#
# strok(g)

# 2 способ
# def f(text):
#
#     text = sorted(text.split())
#     max_len = len(max(text, key=len))
#     for i, value in enumerate(text, 1):
#         print(f'{i:>2}. {value:>{max_len}}')
#
#
# string = input ('введите строку: ')
# f(string)

# 3 способ
def f(text):

    text = sorted(text.split())
    max_len = len(max(text, key=len))
    for i, value in enumerate(text, 1):
        print(f'{i:>2}. {value.rjust(max_len)}')
# .rjust - пробелы справа
# .ljust - пробелы слева

string = input('введите строку: ')
f(string)