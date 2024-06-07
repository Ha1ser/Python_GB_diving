# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# Пример
#
# На входе:
#
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]



text = "Hello world. Hello Python. Hello again."
# # решение 1 - мой код
# text = text.lower().replace("'", " ").replace(".", "").replace(",", "").replace("!", "").split()
# # text = sorted(text, reverse=True)
#
# slov = {}
# k = 0
# LIMIT = 11
#
#
# for i in text:
#     if k <= LIMIT:
#         if str.isdigit(i) == True:
#             continue
#         count = text.count(i)
#         slov[i] = count
#     k += 1
#
#
# print([(k, v) for k, v in slov.items()])

# res = [(k, v) for k, v in slov.items()]


# slov = dict(sorted(slov.items(), key=lambda x: x[1]))
# res = [(k, v) for k, v in slov.items()]
# res = list(reversed(res))
# print(res)

# решение 2
new_text = text.lower().replace("'", " ").replace(".", "").replace(",", "").replace("!", "")
list = new_text.split(' ')
sorted_list = sorted(list, reverse=True)

count_dict = {}

for elem in sorted_list:
    if str.isdigit(elem) == True:
        continue
    count_dict[elem] = sorted_list.count(elem)

print(count_dict)
sorted_count_dict = sorted(count_dict.items(), key = lambda item: item[1], reverse=True)
print(sorted_count_dict)


