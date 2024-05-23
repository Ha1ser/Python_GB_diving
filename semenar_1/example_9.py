# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

low_linmit = 2
up_limit = 10
column = 4

for row in (low_linmit, low_linmit + column):
    for num_2 in range(low_linmit, up_limit + 1):
        for num_1 in range(row, row + column):
            print(f"{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}", end=" \t")
        print()
    print()
