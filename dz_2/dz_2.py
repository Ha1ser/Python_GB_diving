# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.
#
# Пример
#
# На входе:
#
#
# frac1 = "1/2"
# frac2 = "1/3"
# На выходе:
#
#
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

import fractions

frac1 = "1/2"
frac2 = "1/3"


for i in range(len(frac1)):
    if str.isdigit(frac1[i]) == True:
        cis1 = int(frac1[0])
        zn1 = int(frac1[2])


for i in range(len(frac2)):
    if str.isdigit(frac2[i]) == True:
        cis2 = int(frac2[0])
        zn2 = int(frac2[2])

print(f"Сумма дробей: {cis1 * zn2 + cis2 * zn1}/{(zn1 * zn2)}")
print(f"Произведение дробей: {cis1 * cis2}/{(zn1 * zn2)}")


gg = fractions.Fraction(frac1)
wp = fractions.Fraction(frac2)

print(f"Сумма дробей: {gg + wp}")
print(f"Произведение дробей: {gg * wp}")


