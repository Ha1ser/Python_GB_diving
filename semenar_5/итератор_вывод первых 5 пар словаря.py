# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


COUNT = 5
str_1 = 'qwerty'
res = {char: ord(char) for char in str_1}

dict_iter = iter(res.items())
for _ in range(COUNT):
    print(*next(dict_iter)) 