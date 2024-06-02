# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

cmd_exit = "в"
cmd_deposit = "п"
cmd_withdraw = "с"
multiplicity = 50
number_operation = 3
precent_removal = decimal.Decimal(15) / decimal.Decimal(1000)
richness_persent = decimal.Decimal(10) / decimal.Decimal(100)
richness_sum = decimal.Decimal(5_000_000)
min_removal = decimal.Decimal(30)
max_removal = decimal.Decimal(600)
precent_bonus = decimal.Decimal(3) / decimal.Decimal(100)
balanсe = decimal.Decimal(60000000)
count = 0

while True:
    action = input(f"Пополнить - '{cmd_deposit}', снять - '{cmd_withdraw}', выйти - '{cmd_exit}' ")
    if action == cmd_exit:
        print(f"заберите карту. Баланс: {balanсe} у.е")
        break
    if balanсe > richness_sum:
        percent = balanсe * richness_persent
        balanсe -= percent
        print(f"вычтен налог на богатство {richness_persent * 100}%. Сумма процента - {percent}. Баланс - {balanсe}")

    if action in (cmd_deposit, cmd_withdraw):
        amount = 1
        while amount % multiplicity != 0:
            amount = decimal.Decimal(input(f"введите сумму кратную {multiplicity}: "))

        if action == cmd_deposit:
            count += 1
            balanсe += amount
            print(f"Пополнение карты на {amount}. Баланс карты: {balanсe}")
        elif action == cmd_withdraw:
            percent = amount * precent_removal
            percent = min_removal if percent < min_removal else max_removal if percent > max_removal else percent
            sub = amount + percent
            if balanсe > sub:
                balanсe -= sub
                count += 1
                print(f"снятие с карты {amount} у.е. Сумма процента за снятие {percent}. Баланс карты {balanсe}")
            else:
                print(f"недостаточно средств. Сумма снятия {amount}. Сумма процента за снятие {percent}"
                      f"Баланс карты {balanсe}")
        if count % number_operation == 0:
            bonus = balanсe * precent_bonus
            balanсe += bonus
            print(f"Начислен бонус: {bonus} за каждую {number_operation}. Баланс карты {balanсe}")
