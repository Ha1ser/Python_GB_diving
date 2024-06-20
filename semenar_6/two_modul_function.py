# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint

def guess(low_limit: int = 0, upper_limit: int = 100, count: int = 10) -> bool:
    number = randint(low_limit, upper_limit)
    for _ in range(0, count):
        answer = int(input("Input number: "))
        if answer == number:
            return True
        elif answer > number:
            print(f"Число {answer} Больше загадонного")
        else:
            print(f"Число {answer} Меньше загадонного")
    return False


if __name__ == '__main__':
    print(guess())


# как вызывать в других файлах
# import for_two_task

# print(for_two_task.guess(5, 10, 3))
