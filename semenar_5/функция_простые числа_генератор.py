# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def isprime(num):
    prine_num = 2
    count = 1
    yield prine_num
    prine_num += 1
    while count < num:
        for div in range(3, int(prine_num ** 0.5) + 1, 2):
            if prine_num % div == 0:
                break
        else:
            count += 1
            yield prine_num
        prine_num += 2


# более понятный код
def isprime_2(num):
    prine_num = 2
    count = 1
    yield prine_num
    prine_num = 3
    count = 2
    yield prine_num
    while count < num:
        prine_num += 2
        for div in range(3, int(prine_num ** 0.5) + 1, 2):
            if prine_num % div == 0:
                break
        else:
            count += 1
            yield prine_num


print(*isprime(5))

for num in isprime_2(20):
    print(num, end=", ")
