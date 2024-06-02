# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# рещение 1
# spis = [1, 3, 5, 2, 4, 1, 1, 6, 6, 8, 9]
# spis_2 = []
# k = 1
#
# for i in range(len(spis)):
#     if spis[i] % 2 != 0:
#         spis_2.append(k)
#     k += 1
# print(spis_2)

# реш 2
# data = [1, 3, 5, 2, 4, 1, 1, 6, 6, 8, 9]
# unique_list = []
#
# for i, item in enumerate(data, 1):
#     if item % 2 != 0:
#         unique_list.append(i)
# print(unique_list)

# реш 3
data = [1, 3, 5, 2, 4, 1, 1, 6, 6, 8, 9]

new_list = [n for n, elem in enumerate(data, 1) if elem % 2]
print(new_list)

