# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

# реш 1
# data = [1, 1, 2, 2, 2, 3]
#
# unique_list = [item for item in data if data.count(item) != 2]
#
# print(unique_list)

# реш 2
# data = [1, 1, 2, 2, 2, 3]
# unicut_list = []
#
# for i in data:
#     if data.count(i) != 2:
#         unicut_list.append(i)
#
# print(unicut_list)

# реш 3
data = [1, 1, 2, 2, 2, 3]
COUNT = 2

for item in set(data):
    if data.count(item) == COUNT:
        for _ in range(COUNT):
            data.remove(item)
print(data)







