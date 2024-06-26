# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
#
# Пример
#
# На входе:
#
#
# num = 255
# На выходе:
#
#
# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff

num = 255
hex_digits = "0123456789ABCDEF"
hexadecimal = ""
cikl = num

while cikl > 0:
    remainder = cikl % 16
    hexadecimal = hex_digits[remainder] + hexadecimal
    cikl = cikl // 16
print(f"Шестнадцатеричное представление числа: {hexadecimal}")
print(f"Проверка результата: {hex(num)}")



