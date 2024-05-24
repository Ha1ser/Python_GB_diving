from random import randint

num = randint(0, 1000)
k = 1
while k <= 10:
    print(f"{k}.", end=" ")
    n = int(input("введите число от 0 - 1000: "))
    if n == num:
        print(f"число найдено! Программа задумала число: {num}")
        break
    elif n > num:
        print("меньше")
        k += 1
    elif n < num:
        print("больше")
        k += 1
else:
    print("")
    print("Попыток больше не осталось")
