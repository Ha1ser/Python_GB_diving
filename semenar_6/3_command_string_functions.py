# Задание №3
# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

from random import randint
from sys import argv


def quess(low_lim: int = 0, up_limit: int = 100, count: int = 10) -> bool:
    num = randint(low_lim, up_limit)
    for _ in range(count):
        answer = int(input('Введите число: '))
        if answer == num:
            return True
        elif answer > num:
            print(f'Число {answer} больше загаданного')
        elif answer < num:
            print(f'Число {answer} меньше загаданного')
    return False


if __name__ == '__main__':
    params = argv[1:]
    params = (int(num) for num in params)
    print(quess(*params))

# указывать полный путь вклучаю папку