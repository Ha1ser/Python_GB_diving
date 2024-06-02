# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# первый вариант решения
import sys
#
# pn = 1
# l = 0
# data = [1, 2, 4, "qwerty", 10, "tttt", 54.34, (1, 3, 6), (356, "tew", "one"), "bit", 635, 50]
# for i in range(len(data)):
#     print(f"{pn}.", end=" ")
#     if isinstance(data[i], int):
#         print("целое число -> ", end=" ")
#     if isinstance(data[i], str):
#         print("Это строка -> ", end=" ")
#     print(f"{data[i]}| Адрес в памяти: {id(data[i])} | размер в памяти: {sys.getsizeof(data[i])} \
# | хэш объекта: {hash(data[i])}|")
#     pn += 1


# второй вариант решения

data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
for n, item in enumerate(data, 1):
    # print(n, item)
    check_int = "целое число" if isinstance(item, int) else ""
    check_str = "это строка" if isinstance(item, str) else ""
    print(f"{n}. Объект {item}\n адрес: {id(item)}\t размер: {sys.getsizeof(item)}\t"
          f"Хэш: {hash(item)} {check_int}{check_str}")
