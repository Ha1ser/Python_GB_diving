# Инфо из лекции 2

### Строгая динамическая типизация Python

* Функция **type(object)**. Возвращает класс объекта, его тип
* Функция **id(object)**. Возвращает адрес объекта в оперативной памяти
* Функция **isinstance(object, classinfo)**
  Принимает на вход объект и класс и возвращает истину, если объект
  является экземпляром прямого или косвенного подкласса
* Оператор **is**. Сравнивает пару объектов на идентичность(сравнивает тип данных одного числа с другим)

### Хэш как проверка на неизменяемость

**Хеш** — это криптографическая функция хеширования,
которую обычно называют просто хэшем.
**Хеш** — функция представляет собой алгоритм,
который может преобразовать произвольный
массив данных в набор бит фиксированной длины.
Функция **hash(object)**
Возвращает hash объекта в виде целого числа

### объявление переменных

Пример — *data: int = 45* (переменная - тип - значение)

```Python
def funk(data: list[
  int, float]) -> float:  # list[int, float] - хотим чтобы пользователь передовал int or float, другие типы данных передовать нельзя.   -> float - какой тип хотим вернуть 
  res = sum(data) / len(data)
  return res


print(funk([2, 5.5, 15, 8.0, 13.74]))
```

### Атрибуты и методы

*Атрибуты и методы есть практически у всех объектов в Python.*

1. **Атрибуты** — это переменные, конкретные характеристики объекта, такие как цвет поля или имя пользователя.
2. **Методы** — это функции, которые описаны внутри объекта или класса. Они относятся к определенному объекту и
   позволяют взаимодействовать с ними или другими частями кода.

`.__doc__` — показывает информацию об объекте

```Python
print("Hello world!".__doc__)
print(str.__doc__)
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
# 
# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
# 
# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.
```

### Функции для получения информации об атрибутах и методах

* **Функция dir(object)**
  Попытается вернуть список допустимых атрибутов для объекта.
  Если объект не передавать — список имен в текущей локальной области
* **Функция help(object)**
  Если объект не указан, запускается интерактивная справочная система.
  Если аргумент является строкой, то эта строка ищется как имя модуля,
  функции, класса, метода, ключевого слова или раздела документации
  и далее выводится страница справки. Если аргументом является объект
  любого другого типа, создается страница справки по этому объекту.

```Python
print(dir("Hello world!"))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__'     ...
print(dir("Hello world!"))
```

`keywords` — выдает список функций
'symbols' — выдает список символов(+ - = > <)

```Python
help()
# help> keywords — можно получить список ключевых слов, про которые можно узнать информацию если ввести их в help>
```

## Простые» объекты

### Целые числа

* **int(x, base=10)** — возвращает целочисленный
  объект, созданный из числа или строки x ,
  или возвращает значение 0, если аргументы
  не заданы. base — основание системы счисления,
  от 2 до 36.
* **bin(x)** — преобразует целое число в двоичную
  строку с префиксом «0b».
* **oct(x)** — преобразует целое число в
  восьмеричную строку с префиксом «0o».
* **hex(x)**— преобразует целое число в строчную
  шестнадцатеричную строку с префиксом «0x».

## Вещественные числа

* **float(x)** — возвращает число с плавающей
  запятой, составленное из числа или строки x.

## Логические типы

* **bool(x)** — возвращает логическое значение,
  т.е. одно из двух: True или False.

## Строки и способы их записи

**Виды кавычек:**

* `txt = 'Книга называется "Война и мир".'`
* `class str(object):`
* `"""текст"""`

```Python
f = """ # можно в переменную присваивать несколько строк текста благодоря тройным кавычкам
qwerty
jdsnmkblfd
gfdbf
befsv
"""
```

**склеивание строк:**

```Python
text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)  # Привет.Как ты, друг?Рад тебя видеть.

x = 'fdsf '
'dsffd '
'bsdf'

print(x)  # fdsf dsffd bsdf


```

## Математические модули

### Модуль math

**Константы**: e, inf, nan, pi, tau

**Математические функции**: acos, acosh, asin, asinh,
atan, atan2, atanh, ceil, comb, copysign, cos, cosh,
degrees, dist, erf, erfc, exp, expm1, fabs, factorial, floor,
fmod, frexp, fsum, gamma, gcd, hypot, isclose, isfinite,
isinf, isnan, isqrt, lcm, ldexp, lgamma, log, log10, log1p,
log2, modf, nextafter, perm, pow, prod, radians,
remainder, sin, sinh, sqrt, tan, tanh, trunc, ulp

### Модуль decimal

* **num = decimal.Decimal(object)** Получаем вещественное число с точностью 28 знаков (до и после запятой).
* **decimal.getcontext().prec = dec** Задаём точность в dec знаков для будущих операций.

### Модуль fraction

**Запись дробей вида ⅓, ⅗ и т.п.**

```Python
import fractions

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)  # 1/3 3/5 1/5
```

### Комплексные числа

**complex([real[, imag]])** — комплексное число
из действительной real и мнимой imag частей.

```Python
a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')
# (2+3j)
# (2+3j)
# True
```

### Математические функции «из коробки»

* **abs(x)** — возвращает абсолютное значение числа x,
  число по модулю.
* **divmod(a, b)** — функция принимает два числа
  в качестве аргументов и возвращает пару чисел —
  частное и остаток от целочисленного деления.
  Аналогично вычислению a // b и a % b.
* **pow(base, exp[, mod])** — при передаче 2-х аргументов
  возводит base в степень exp. При передаче 3-х
  аргументов, результат возведения в степень делится
  по модулю на значение mod.
* **round(number[, ndigits])** — округляет число
  number до ndigits цифр после запятой. Если второй
  аргумент не передать, округляет до ближайшего целого.

# Инфо из лекции 3

# Коллекции

## списки

**создание списков:**

```python
list_1 = list()
list_2 = list((3.14, True, "hello world"))
list_3 = []
list_4 = [3.14, True, "hello world"]
```

**методы:**

1. `append()` - Добавление одного элемента в конец
2. `extend()` - Добавление нескольких элементов в конец

```Python
g = []
st = "qwerty"
g.extend(st)
print(g)  # ['q', 'w', 'e', 'r', 't', 'y']
```

3. `pop()` - Удаление элемента по индексу
4. `count()` - Подсчёт вхождения элемента
5. `index()` - Индекс первого вхождения элемента(в скобках значение, возвращает индекс)
6. `insert()` - Вставка элемента по индексу
7. `remove()` - Удаление элемента по значению

**Сортировки и развороты**

* `функция sorted()`

```Python
my_list = [4, 5, 2, 7, 1, 6, 8, 3, 9]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
# [4, 5, 2, 7, 1, 6, 8, 3, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
# [4, 5, 2, 7, 1, 6, 8, 3, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

* `метод sort()`

```Python
my_list = [4, 5, 2, 7, 1, 6, 8, 3, 9]
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.sort(reverse=True)
print(my_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**Разворот:**

* `Функция reversed()`

```Python
my_list = [4, 5, 2, 7, 1, 6, 8, 3, 9]
res = list(reversed(my_list))
print(res)
```

* `Метод reverse()`

```Python
my_list = [4, 5, 2, 7, 1, 6, 8, 3, 9]
my_list.reverse()
print(my_list)
```

**Создание копий**

* `Метод copy()` - Создаёт поверхностную копию
* `Функция copy.deepcopy()` - Рекурсивно создаёт полную копию

**Функция len()**

* `len(x)` — возвращает целое число — количество элементов коллекции.
* Не учитывает вложенные коллекции!

## строки, str

`.replace()` - замена

```python
text = "Hello world"
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 1)
print(text, new_txt, sep="\n")
# w
# lo w
# Hello world
# HeLlo world
```

* `count()` - Подсчёт вхождения элемента
* `index()` - Индекс первого вхождения элемента
* `find()` - Индекс первого вхождения элемента(отличие от index() в том что если искомого элемента нет в строке, то find
  возращает -1 в index() выдает ошибку)


* разворот строки:

```python 
text = "Hello world"
print(text[::-1])  # dlrow olleH
```

## Форматирование строк

1. `Форматирование через %` - Старый способ, сохранился в некоторых модулях

```python
name = 'qwerty'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)  # %s - строка, %d - число
print(text)
# Меня зовут qwerty и мне 12 лет
```

2. `Метод format()` - Строковой метод, заменяющий фигурные скобки на переменные

```python
name = 'qwerty'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)
```                                                  

3. `f-строка` - Сочетание неизменяемого текста и переменных в фигурных скобках

```python
name = 'qwerty'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)
```     

## Строковые методы

1. `split()` - Разбивает строку на отдельные элементы

```python
link = 'qw://er//t/y/'
er = link.split('/')
print(er)  # ['qw:', '', 'er', '', 't', 'y', '']

a, b, c = input('введите 3 числа через пробел: ').split()
print(a, b, c)  # введите 3 числа через пробел: 5 6 4 

a, b, c, *_ = input('введите не менее трех чисел через пробел: ').split()
print(a, b, c)  # введите не менее трех чисел через пробел: 543 235345 23534 3245 23353 2335
# 543 235345 23534
```

2. `join()` - Формирует строку из отдельных элементов

```Python
data = ['qw:', '', 'er', '', 't', 'y', '']
url = '/'.join(data)
print(url) 
``` 

3. `upper(), lower(), title(), capitalize()` - Изменение регистра

```Python
data = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(data.title())  # каждое слово начинается с заглавной буквы
print(data.capitalize())  # первое слово начинается с заглавной буквы
# Однажды В Студёную Зимнюю Пору
# Однажды в студёную зимнюю пору
```   

4. `startswith() и endswith()` - Проверка на совпадение с началом или концом строки

```Python
text = 'однажды в СТУДЁНУЮ зимнюю ПоРУ'
print(text.startswith('однажды'))
print(text.endswith('зимнюю', 0, -5))  # можно указывать аргументы от какого до какого...
# True 
# True
```

## Кортежи, tuple

**Способы создания кортежа**

```Python
a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1, c2, d, sep='\n')
# ()
# (1,)
# (1,)
# (1, 2, 3)
# (1, 2, 3)
# (0, 1, 2)
```

## Словари, dict

**Создание словаря**

```Python 
a = {'one': 42, 'two': 3.14, 'ten': 'Hello word!'}
b = dict(one=42, two=3.14, ten="Hello word!")
c = dict([('one', 42), ('two', 3.14), ('ten', "Hello word!")])
print(a == b == c)  # True
```

**Доступ к значению словаря**

* `dict[key]` — доступ через квадратные скобки []
* `dict.get(key[, default])` — доступ через метод get()

```Python 
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
print(a['two'])  # 3.14

# доступ через метод get:
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}

print(a.get('two'))
print(a.get('five'))
print(a.get('five', 5))
print(a.get('ten', 8))
```

**методы для словарей**

* `setdefault()` - Возвращает значение и добавляет ключ в словарь(если указать ключ и еще аргумент справа, то если
  данного ключа нет в словаре, то он будет добавлен в словарь и выведет знач. Иначе если есть в словаре, то просто
  выведет знач, игнорируя указанный аргуметнт)

```Python
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}

s = a.setdefault('five')
print(f'{s = }\t{a=}')  # s = None	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None}
eggs = a.setdefault('six', 6)
print(f'{eggs = }\t{a=}')  # eggs = 6	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
new = a.setdefault('two')
print(f'{new = }\t{a=}')  # new = 3.14	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
new_t = a.setdefault('one', 1_000)
print(f'{new_t = }\t{a=}')  # new_t = 42	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
```

* `keys()` - возвращает объект-итератор dict_keys

```Python
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
print(a.keys())

for key in a.keys():
  print(key)
# dict_keys(['one', 'two', 'four', 'ten'])
# one
# two
# four
# ten 
```

* `values()` - возвращает объект-итератор dict_values(возвращает значения)

```Python
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
print(a.values())

for value in a.values():
  print(value)
# dict_values([42, 3.14, 4, 10])
# 42
# 3.14
# 4
# 10
```

* `items()` - возвращает объект-итератор dict_items

```Python
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
print(a.items())
# dict_items([('one', 42), ('two', 3.14), ('four', 4), ('ten', 10)])


a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
for key, value in a.items():
  print(f"{key = } value before - {100 - value}")
# key = 'one' value before - 58
# key = 'two' value before - 96.86
# key = 'four' value before - 96
# key = 'ten' value before - 90        
```

* `popitem()` - Удаляет последнюю пару ключ-значение

```Python
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')
# spam = ('ten', 10)	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4}
# eggs = ('four', 4)	my_dict={'one': 1, 'two': 2, 'three': 3}
```

* `pop()` - Удаляет пару ключ-значение по ключу

```Python
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')  # spam = 2 my_dict={'one': 1, 'three': 3, 'four': 4, 'ten': 10}
err = my_dict.pop('six')  # будет ошибка т.к six не существует в словаре
err = my_dict.pop()  # будет ошибка т.к не чего не передаем в .pop()
```

* `update()` - Расширяет исходный словарь новыми парами

```Python
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'six': 6}
# {'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'six': 6, 'five': 5}

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)
# {'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'five': 5, 'six': 6}
```

## Множества, set и frozenset

* **my_set = {1, 2, 3, 4, 2, 5, 6, 7} - Изменяемое множество**
* **my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,)) - Неизменяемое множество**

**методы:**

* add() - Добавляет элемент

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(9, 10)
print(my_set)  # TypeError: set.add() takes exactly one\
```

* remove() - Удаляет элемент

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)  # {1, 2, 3, 4, 6, 7}
my_set.remove(10)  # KeyError: 10
```

* discard() - Удаляет элемент

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)  # {1, 2, 3, 4, 6, 7}
my_set.discard(10)
print((my_set))  # {1, 2, 3, 4, 6, 7} ошибки нет
```

* intersection() - Пересечение множеств

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# my_set = {1, 2, 3, 4, 5, 6, 7}
# other_set = {1, 42, 4, 314}
# new_set = {1, 4}

# & в место .intersection()

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# my_set = {1, 2, 3, 4, 5, 6, 7}
# other_set = {1, 42, 4, 314}
# new_set = {1, 4}
```                                       

* union() - Объединение множеств, |

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

# | в место .union()
new_set_2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
```

* difference() - Разность множеств, -(выводятся уникальные множества)

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# my_set = {1, 2, 3, 4, 5, 6, 7}
# other_set = {1, 42, 4, 314}
# new_set = {2, 3, 5, 6, 7}


# - в место .difference()
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
# my_set = {1, 2, 3, 4, 5, 6, 7}
# other_set = {1, 42, 4, 314}
# new_set_2 = {2, 3, 5, 6, 7}
```

## Проверка на вхождение, in

*Зарезервированное слово in позволяет сделать проверку на вхождение элемента в коллекцию.*

```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
print(42 in my_set)  # False
print(5 in my_set)  # True
```

## Байты, bytes и bytearray

```Python
text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))  # b'Hello world!' <class 'bytes'>

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!' <class 'bytes'>

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')  # 
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(x)  # b'\xd0\x9f\xd1\x80\xd0\xb8'
print(y)  # bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')                
```

# Инфо из лекции 4
## Функции

*Функция — фрагмент программного кода, к которому можно
обратиться из другого места программы.*

### Функция высшего порядка
*Функцией высшего порядка называется такая функция, которая принимает функцию-объект
как аргумент или возвращает функцию-объект в виде выходного значения.*

* **Функция() — вызываем** -  print(42)
* **Функция — передаём** - func = sum

### Определение собственной функции
*Зарезервированное слово **def***

### Что такое pass?
*Зарезервированное слово pass ничего не делает*
```Python
if a == 5:
    a += 1
else:
 pass
```

### Возврат значения из функции, return
* Если указан один объект после return - возвращается именно этот объект
* Если указано несколько значений через запятую после return - возвращается кортеж с перечисленными значениями
* Если ничего не указано после return - возвращается None
* Если return отсутствует - Python «мысленно» дописывает в качестве последней строки функции *return None*

### Значения по умолчанию
После параметра указываем значения по умолчанию
```Python
def quadratic_equations(a, b=0, c=0):
```
* В качестве значения по умолчанию нельзя указывать изменяемы типы: списки, словари, множества и т.п.!

### Позиционные и ключевые параметры 

*Косая черта / и звёздочка * разделяют позиционные и ключевые параметры*

```Python
def func(positional_only, /, positional_or_keyword, *, keyword_only):
    pass
```
* Позиционные параметры - это параметры, которые передаются в функцию в том же порядке, в котором они объявлены. 
Они являются обязательными для указания при вызове функции.
* Ключевые параметры - это параметры, которые передаются в функцию указанием их имени. 
* Они могут быть переданы в любом порядке, и могут иметь значения по умолчанию.

### Параметры *args и **kwargs 
*Имена args и kwargs — общепринятое соглашение*
* def func(*args): — принимает любое число
позиционных аргументов
* def func(**kwargs): — принимает любое
число ключевых аргументов
* def func(*args, **kwargs): — принимает любое
число позиционных и ключевых аргументов

### Области видимости
* **Локальная** Код внутри самой функции, т.е. переменные заданные в теле функции
* **Глобальная, global** Код модуля, т.е. переменные заданные в файле py содержащем функцию
* **Не локальная, nonlocal** Код внешней функции, исключающий доступ к глобальным переменным


### Анонимная функция lambda
* **lambda parameters: action**
*Анонимные функции, они же лямбда функции — синтаксический сахар для
обычных питоновских функций с рядом ограничений. Они позволяют задать
функцию в одну строку кода без использования других ключевых слов.*

### Документирование кода функций
Пишется сразу после определения функции. Пояснения к однострочной строке документации:
* Тройные кавычки используются, даже если строка помещается на одной строке. Это позволяет легко расширить его позже.
* Закрывающие кавычки находятся на той же строке, что и открывающие. Это выглядит лучше для однострочников.
* Нет пустой строки ни до, ни после строки документации.
* Строка документации — это фраза, заканчивающаяся точкой. Он описывает действие функции или метода как команду.
* Однострочная строка документации не должна повторять параметры функции.
* 
*если вызвать функцию help() и в скобках указать название функции, то будет представлена документация к функции.*

## Встроенные функции
*В Python есть ряд встроенных функций. Перечислим их в алфавитном порядке:*

**abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(),
bytearray(), bytes(), callable(), chr(), classmethod(), compile(), complex(),
delattr(), dict(), dir(), divmod(), enumerate(), eval(), exec(), filter(), float(),
format(), frozenset(), getattr(), globals(), hasattr(), hash(), help(), hex(), id(),
input(), int(), isinstance(), issubclass(), iter(), len(), list(), locals(), map(),
max(), memoryview(), min(), next(), object(), oct(), open(), ord(), pow(), print(),
property(), range(), repr(), reversed(), round(), set(), setattr(), slice(), sorted(),
staticmethod(), str(), sum(), super(), tuple(), type(), vars(), zip().**

* **map(function, iterable)** - Принимает на вход функцию и последовательность. Функция применяется к каждому элементу 
последовательности и возвращает map итератор.
* **filter(function, iterable)** - Принимает на вход функцию и последовательность. 
Если функция возвращает истину, элемент остаётся в последовательности. Как и map возвращает объект итератор.
* zip(*iterables, strict=False) - Принимает несколько последовательностей и итерируется по ним параллельно. 
Если передать ключевой аргумент strict=True, вызовет ошибку ValueError в случае разного 
числа элементов в каждой из последовательностей.
```Python
# для zip
names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salari, award in zip(names, salaries, awards):
    print(f"{name} заработал {salari:.2f} денег и премию {salari * award:.2f}")
```

* `max(iterable, *[, key, default])или max(arg1, arg2, *args[, key])` - Функция принимает на вход 
итерируемую последовательность или несколько позиционных элементов и ищет максимальное из них.
```Python
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default="none")) # none
print(max(*lst_2)) # 256
print(max(lst_3, key=lambda x: x[1])) # ('Иван', 125000)
```
* `min(iterable, *[, key, default])` или min(arg1, arg2, *args[, key]) - Функция работает аналогично
max, но ищет минимальный элемент.
* `sum(iterable, /, start=0)` - Функция принимает объект итератор и подсчитывает сумму всех элементов. 
Ключевой аргумент start задаёт начальное значение для суммирования.
```Python
lst_2 = [42, 256, 73]
print(sum(lst_2)) #371
print(sum(lst_2, start=1024)) #1395
```

* `all(iterable)` - Функция возвращает истину, если все элементы последовательности являются истиной.
```Python
def all_(iterable):
    for element in iterable:
        if not element:
            return False
        return True

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print("все элетенты положительные")
else:
    print("есть отрицательные элементы или нули")
# есть отрицательные элементы или нули
```
* `any(iterable)` - Функция возвращает истину, если хотя бы один элемент последовательности являются истиной.
```Python
def all_(iterable):
    for element in iterable:
        if not element:
            return False
        return True

numbers = [-42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print("хотябы один элемент положительный")
else:
    print("все элементы не больше 0")
# хотябы один элемент положительный
```

* `chr(integer)` Функция возвращает строковой символ из таблицы Юникод по его номеру. Номер — целое число от 0 до 1_114_111.
* `ord(char)` Функция принимает один символ и возвращает его код в таблице Юникод. 
```Python
print(chr(97)) #а
print(chr(1105)) #ё 
print(chr(128519)) #😇

print(ord("a")) # 97
print(ord("ё")) #1105
print(ord("😇")) #128519
```

* `locals()` Функция возвращает словарь переменных из локальной области видимости на момент вызова функции.
```Python
def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z 

func(1, 2, 3) 
# {'a': 1, 'b': 2, 'c': 3, 'x': 3}
```
* `globals()` Функция возвращает словарь переменных из глобальной области видимости, т.е. из пространства модуля.
* `vars()` Функция без аргументов работает аналогично функции locals(). Если передать в vars объект,
функция возвращает его атрибут__dict__. А если такого атрибута нет у объекта, вызывает ошибку TypeError.

# Инфо из лекции 5(Итераторы и генераторы)
## Однострочники

`a, b = b, a`
```Python
a = 1
b = 2
a, b = b, a
print(f"{a = }\t{b = }") # a = 2	b = 1
```

### Распаковка
*Варианты распаковки значений*
* `Обычная распаковка - a, b, c = последовательность`
```Python
a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')
# Три символа: 123
# a='1' b='2' c='3'
```
* `Распаковка с упаковкой - a, *b, c = последовательность`
```Python
data = ["1", "3", "4", "6", "9", "2", "10"]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')                                                                        
# a='1' b='3' c='4' d=['6', '9', '2', '10'] 

data = ["1", "3", "4", "6", "9", "2", "10"]
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
# a='1' b='3' c=['4', '6', '9', '2'] d='10'

data = ["1", "3", "4", "6", "9", "2", "10"]
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
# a=['1', '3', '4', '6'] b='9' c='2' d='10'
```
* `Распаковка со звёздочкой - *последовательность` 

## Итераторы
`iter(object[, sentinel])` - Функция принимает на вход object поддерживающий итерацию. 
Второй параметр функции iter — sentinel передают для вызываемых объектов-итераторов

```Python
data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)
#<list_iterator object at 0x000001965E851690>

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)
#2 4 6 8
```

`next(iterator[, default])` - На вход функция принимает итератор, который вернула функция iter. 
Второй параметр функции next — default нужен для возврата значения по умолчанию вместо выброса исключения StopIteration.
```Python
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter)) # 2
print(next(list_iter)) # 4
print(next(list_iter)) # 6
print(next(list_iter)) # 8
print(next(list_iter)) # ошибка StopIteration

# второй параметр next
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42)) # 2
print(next(list_iter, 42)) # 4
print(next(list_iter, 42)) # 6
print(next(list_iter, 42)) # 8
print(next(list_iter, 42)) #42
print(next(list_iter, 42)) # 42
# в место ошибок выводятся дефолтные значения - 42 
```
## Генераторы

**Генераторные выражения** - Генераторные выражения Python позволяют создать собственный генератор, перебирающий значения.
```Python
my_gen = (chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char, end=" ")
# <generator object <genexpr> at 0x000001A40915DB10>
# a b c d e f g h i j k l m n o p q r s t u v w x y z 
```

**List comprehensions** - list_comp = [expression for expr in sequense1 if condition1 ...]
*Генератор списков формирует list заполненный данным и присваивает его переменной.*
```Python
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f"{res = }") # res = [2, 42, 76, 24]
```

**Set и dict comprehensions**
* **Set comprehensions** - set_comp = {expression for expr in sequense1 if condition1 …}
* **Dict comprehensions** - dict_comp = {key: value for expr in sequense1 if condition1 …}
* **Сходства и различия** - {используются фигурные скобки для выражения} словарь подставляет ключ и значение через двоеточие

**Команда yield** - Команда yield работает аналогично return. Но вместо завершения функции запоминает её состояние.
Повторный вызов продолжает код после yield.
```Python
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(5), start=1):
    print(f"{i}! = {num}")
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
```

*Функции iter и next одинаково работают с генераторами «из коробки» и с созданными самостоятельно.*
```Python
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 6
print(next(my_iter)) # 24
print(next(my_iter)) # StopIteration
```

# Инфо из лекции 6(Модули)

* `import module_name` - Строки импорта рекомендуется писать в самом начале файла,
оставляя 1-2 пустые строки после него.
* `import from` - from sys import builtin_module_names
* `import as` - import numpy as np
* `import *` - from имя_модуля import *, Подобная запись импортирует из модуля все глобальные объекты за исключением тех,
чьи имена начинаются с символа подчёркивания.(Плохой import)
*  `__all__` -  `__all__ = ['func', '_secret', '...']`, Cписок имён объектов, заключённых в кавычки,
т.е. строки для импорта через «звёздочку».

## Виды модулей 
### Встроенные модули
* Стандартная библиотека устанавливается вместе с интерпретатором. 
Дополнительные манипуляции по установке не требуются. Всё работает «из коробки».
* Для использования модуля стандартной библиотеки достаточно его импортировать в ваш код.
* Большинство частых задач легко решаются средствами стандартной библиотеки. Достаточно обратиться к справке и найти нужный модуль.
* Некоторые модули стандартной библиотеки разрабатывались настолько давно, что не отвечают современным требованиям решения задач.
В таком случае на помощь приходят внешние решения. И наоборот. Каждое обновление Python вносит улучшения в библиотеку, зачастую более
эффективные, чем внешние решения. 

### Свои модули
* Документация по модулю в виде многострочного комментария (три пары двойных кавычек),
* Импорт необходимых пакетов, модулей, классов, функций и т.п. объектов,
* Определение констант уровня модуля,
* Создание классов модуля при ООП подходе,
* Создание функций модуля,
* Определение переменных модуля,
* Покрытие тестами, если оно не вынесено в отдельный пакет,
* Main код.


* `__name__ == '__main__'` - Магическая переменная __name__ содержит полное имя импортируемого модуля или '__main__'


```Python
#...
if __name__ == '__main__':
 print('Starting main code')
# ...
```

## Создание пакетов и их импорт
`Файл __init__.py` - Директоия с __init__.py превращается в пакет

### Разница между модулем и пакетом
**Пакет хранит модули.**
* Пакет — директория с `__init__.py` файлом
* Пакет можно импортировать как модуль
* Внутри файл `__init__.py` можно прописать код,
который будет выполняться при импорте пакета.

### Варианты импорта
1. Простой импорт - `import mathematical`
2. Абсолютный импорт
```Python
from mathematical import base_math as bm

from mathematical.advanced_math
import exp
```
3. Относительный импорт
```Python
from . import other_module
from .. import other_module
from ..other_package import
other_module
```

## Некоторые модули «из коробки»
### Модуль sys и запуск скрипта с параметрами
*Модуль sys обеспечивает доступ к некоторым переменным, используемым или поддерживаемым
интерпретатором, а также к функциям, тесно взаимодействующим с интерпретатором.*
```Python
# Код файла:
from sys import argv

print('start')
print(argv)
print('stop')

# Команда запуска: "в командной строке"
# python script.py -d 42 -s "Hello world!" -k 100
```

### Модуль random
*Модуль используется для генерации псевдослучайных чисел.*
* `random()` — генерирует псевдослучайные числа в диапазоне [0, 1)
* `seed(a=None, version=2)` — инициализирует генератор. Если значение a не указано, для инициализации используется текущее время ПК
* `getstate()` — возвращает объект с текущим состоянием генератора
* `setstate(state)` — устанавливает новое состоянии генератора, принимая на вход объект, возвращаемый функцией getstate

**Элементы из random:**
* `randint(a, b)` - целое число от a до b
* `uniform(a, b)` - вещественное число от a до b
* `choice(seq)` - случайный элемент последовательности
* `randrange(start, stop[, step])` - число из диапазона
* `shuffle(x)` - перемешиваем коллекцию x in place
* `sample(population, k, *, counts=None)` - Выборка в k элементов из population

# Инфо из лекции 7(Файлы и файловая система)
## Файлы

`open()` - В Python для получения доступа файлу используют функцию open()
```Python
# пример: 
open(file, mode='r', buffering=-1,
encoding=None,
 errors=None, newline=None, closefd=True,
opener=None)
```

## Режимы работы с файлами

* 'r' — открыть для чтения (по умолчанию)
* 'w' — открыть для записи, предварительно очистив файл
* 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
* 'a' — открыть для записи в конец файла, если он существует
* 'b' — двоичный режим
* 't' — текстовый режим (по умолчанию)
* '+' — открыты для обновления (чтение и запись)

`.close()` - закрывает работу с файлом. Если в коде отсутствует метод close(), то даже при успешном завершении
программы не гарантируется сохранение всех данных в файле

## Прочие необязательные параметры функции open
* buffering — определяет режим буферизации
* errors — используется только в текстовом режиме и определяет поведение в случае ошибок
кодирования или декодирования
* newline — отвечает за преобразование окончания строки
* closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
* opener — позволяет передать пользовательскую функцию для открытия файла

## Менеджер контекста with open 
```Python
with open('text_data.txt', 'r+', encoding='utf-8') as f:
print(list(f))
```
* with гарантирует закрытие файла и сохранение информации

## Чтение файла
1. `list(f)` - Чтение в список
```Python
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    print(list(f)) # ['Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и учебных текстов. Для этого созданы другие замечательные учебники.']
```
2. `res = f.read()` - Чтение методом read
```Python
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')
# Читаем первый раз
# Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
# Читаем второй раз
# 
#
```
```Python
# выводит по 50 символов, задействуется меньше оперативной памяти
size = 50
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    while res := f.read(size):
        print(res) 
# Эта книга адресована всем, кто изучает русский язы
# к. Но состоит она не из правил, упражнений и учебн
# ых текстов. Для этого созданы другие замечательные
#  учебники.
```
3. `res = f.readline()` - Чтение методом readline
```Python
# между каждой строкой есть пустая строка это делает .readline()
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)
# Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил,
# 
# упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
```
```Python
size = 50
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    while res := f.readline(size):
        print(res)
# Эта книга адресована всем, кто изучает русский язы
# к. Но состоит она не из правил,
# 
# упражнений и учебных текстов. Для этого созданы др
# угие замечательные учебники.                                                
```
4. `for line in f:` - Чтение циклом for
```Python
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
# Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил,
# упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
```
```Python
size = 50
with open("qwerty.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))                                                                            
# Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил,
# Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил,
# упражнений и учебных текстов. Для этого созданы другие замечательные учебники
# упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
```
## Запись и добавление в файл
* w - создаём новый пустой файл для записи. Если файл существует, открываем его для записи и удаляем данные, которые в нём
хранились
* x - создаём новый пустой файл для записи. Если файл существует, вызываем ошибку
* a - открываем существующий файл для записи в конец, добавления данных. Если файл не существует, создаём новый файл
и записываем в него

* `res = f.write(text)` - Запись методом write
```Python
text = "this text will add"
with open("qwerty.txt", 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
# res = 18
# len(text) = 18
# фраза добавилась в конец файла
```
```Python
text = ['abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz']
with open("qwerty.txt", 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(text) = }')
# res = 27
# len(text) = 3
# res = 27
# len(text) = 3
# res = 27
# len(text) = 3
# в файл запишется текст в 3 строки благодаря \n в res 
``` 
* `f.writelines('\n'.join(text))` - Запись методом writelines
```Python
text = ['abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz']
with open("qwerty.txt", 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
# .writelines добавил построчно каждый элемент в файл.
```
* `print(text, file=f)` - print в файл
```Python
text = ['abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz']
with open("qwerty.txt", 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
# print(line, file=f) добавляет список в файл построчно каждый элемент и в конце добавляет одну пустую строку
```
```Python
text = ['abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz',
        'abcdifghijklmnopqrstuvwxyz']
with open("qwerty.txt", 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
# в конце каждой строки будут ***, а в начале ##
```

## Методы перемещения в файле
* `f.tell()` - Метод tell возвращает текущую позицию в файле
* `seek(offset, whence=0)` - **offset** — смещение относительно опорной точки, **whence** — способ выбора опороной точки.
  * whence=0 — отсчёт от начала файла
  * whence=1 — отсчёт от текущей позиции в файле
  * whence=2 — отсчёт от конца файла
* `truncate(size=None)` - Метод изменяет размер файла. Если не передать значение в параметр size будет удалена
часть файла от текущей позиции до конца

# Файловая система
## Работа с каталогами
* Определить текущий каталог
```Python
import os
from pathlib import Path

print(os.getcwd()) # C:\Users\User\Desktop\Python_GB_diving
print(Path.cwd()) # C:\Users\User\Desktop\Python_GB_diving
# получили инфу о директории в которой находимся.
```
```Python
import os
from pathlib import Path
print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
# C:\Users\User\Desktop\Python_GB_diving
# C:\Users\User\Desktop\Python_GB_diving
# C:\Users\User
# C:\Users\User
```
* Создать новый каталог
```Python
import os
from pathlib import Path

os.mkdir('new_os_dir') # создается папка 'new_os_dir'
Path('new_path_dir').mkdir() # создается папка 'new_path_dir'
```
```Python
import os
from pathlib import Path
os.makedirs('dir/other_dir/new_os_dir') # создался каталог 'dir/other_dir/new_os_dir'
Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True) # создался каталог 'some_dir/dir/new_path_dir'
```
* Удалить существующий каталог
```Python
import os
from pathlib import Path
# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir') # удаляем папку new_os_dir
Path('some_dir/dir/new_path_dir').rmdir()  # удаляем папку new_path_dir
# Удалить можно лишь пустой каталог. Если внутри удаляемого
# каталога есть другие каталоги или файлы, возникнет ошибка OSError. 
```
```Python
import shutil
shutil.rmtree('dir/other_dir') # удалился каталог dir
shutil.rmtree('some_dir') # удалился каталог some_dir 
```
* Формирование пути
```Python
import os
from pathlib import Path
file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
```

## Чтение данных о каталогах
* Получение списка каталогов и файлов
```Python
import os
from pathlib import Path

print(os.listdir())
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
```
* Проверка на директорию, файл и ссылку
```Python
import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')
    
p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')
# os.path.isdir(obj) = True	os.path.isfile(obj) = False	os.path.islink(obj) = False	obj = '.fold'
# os.path.isdir(obj) = True	os.path.isfile(obj) = False	os.path.islink(obj) = False	obj = '.git'
# os.path.isdir(obj) = False	os.path.isfile(obj) = True	os.path.islink(obj) = False	obj = '.gitignore'
# os.path.isdir(obj) = True	os.path.isfile(obj) = False	os.path.islink(obj) = False	obj = '.idea'
# ...
```
* Обход папок через os.walk()
```Python
import os
for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
```

## Работа с файлами 
* Переименование файлов 
```python
import os
from pathlib import Path

os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py')
p.rename('new_file.py')
# ↕ одно и тоже                                                                                                                       
Path('new_file.py').rename('newest_file.py')
```
* Перемещение файлов
```python
import os
from pathlib import Path

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py')) # переносим файл 'newest_file.py' в каталог 'dir' и меняем название файла на 'new_name.py'

old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file) # перемещаем файл new_name.py в папку new_os_dir.
```
* Копирование файлов
```python
import shutil
shutil.copy('one.txt', 'dir') # копирование файла 'one.txt' в директорию 'dir', если каталога не существует то имя файла изменится на dir
shutil.copy2('two.txt', 'dir/one_more.txt') # копирование файла 'two.txt' в директорию 'dir' и изменяется имя файла на one_more.txt
```
```python
import shutil
import shutil

shutil.rmtree('dir', 'one_more_dir') # копирование директории 'dir' и присвоение имени 'one_more_dir'
```
* Удаление файлов
```python
import shutil

shutil.rmtree('dir') # удаление директории 'dir'
```
```python
import os
from pathlib import Path
os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
```

