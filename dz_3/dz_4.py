# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# Пример
#
# На входе:
#
#
# lst = [1, 1, 2, 2, 3, 3]
# На выходе:
#
#
# [1, 2, 3]

lst = [1, 2, 3, 4, 5]
lst_2 = list()

for i in lst:
    if lst.count(i) > 1:
        lst_2.append(i)
print(list(set(lst_2)))



