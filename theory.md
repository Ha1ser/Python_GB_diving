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
def funk(data: list[int, float]) -> float: #list[int, float] - хотим чтобы пользователь передовал int or float, другие типы данных передовать нельзя.   -> float - какой тип хотим вернуть 
    res = sum(data) / len(data)
    return res

print(funk([2, 5.5, 15, 8.0, 13.74]))
```
### Атрибуты и методы
*Атрибуты и методы есть практически у всех объектов в Python.*
1. **Атрибуты** — это переменные, конкретные характеристики объекта, такие как цвет поля или имя пользователя.
2. **Методы** — это функции, которые описаны внутри объекта или класса. Они относятся к определенному объекту и позволяют взаимодействовать с ними или другими частями кода.

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
*  **Функция help(object)**
Если объект не указан, запускается интерактивная справочная система.
Если аргумент является строкой, то эта строка ищется как имя модуля,
функции, класса, метода, ключевого слова или раздела документации
и далее выводится страница справки. Если аргументом является объект
любого другого типа, создается страница справки по этому объекту.

```Python
print(dir("Hello world!")) 
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__'     ...
print(dir("Hello world!"))
```

`keywords` — выдает список функций 
'symbols' — выдает список символов(+ - = > <)
```Python
help()
    #help> keywords — можно получить список ключевых слов, про которые можно узнать информацию если ввести их в help>
```

## Простые» объекты
### Целые числа
* **int(x, base=10)** — возвращает целочисленный
объект, созданный из числа или строки x ,
или возвращает значение 0, если аргументы
не заданы. base — основание системы счисления,
от 2 до 36.
*  **bin(x)** — преобразует целое число в двоичную
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
print(text) #Привет.Как ты, друг?Рад тебя видеть.

x = 'fdsf '\
    'dsffd '\
    'bsdf'

print(x) #fdsf dsffd bsdf


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
print(f1 * f2) # 1/3 3/5 1/5
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
print(g) #['q', 'w', 'e', 'r', 't', 'y']
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
print(my_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.sort(reverse=True)
print(my_list) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
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
* `find()` - Индекс первого вхождения элемента(отличие от index() в том что если искомого элемента нет в строке, то find возращает -1 в index() выдает ошибку)


* разворот строки:
```python 
text = "Hello world"
print(text[::-1]) #dlrow olleH
```

## Форматирование строк
1. `Форматирование через %` - Старый способ, сохранился в некоторых модулях
```python
name = 'qwerty'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age) # %s - строка, %d - число
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
print(er) # ['qw:', '', 'er', '', 't', 'y', '']

a,b,c = input('введите 3 числа через пробел: ').split()
print(a, b, c) # введите 3 числа через пробел: 5 6 4 

a,b,c, *_ = input('введите не менее трех чисел через пробел: ').split()
print(a,b,c) #введите не менее трех чисел через пробел: 543 235345 23534 3245 23353 2335
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
print(data.title()) # каждое слово начинается с заглавной буквы
print(data.capitalize()) # первое слово начинается с заглавной буквы
# Однажды В Студёную Зимнюю Пору
# Однажды в студёную зимнюю пору
```   
4. `startswith() и endswith()` - Проверка на совпадение с началом или концом строки
```Python
text = 'однажды в СТУДЁНУЮ зимнюю ПоРУ' 
print(text.startswith('однажды'))
print(text.endswith('зимнюю', 0, -5)) # можно указывать аргументы от какого до какого...
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
print(a == b == c) # True
```

**Доступ к значению словаря**
* `dict[key]` — доступ через квадратные скобки []
* `dict.get(key[, default])` — доступ через метод get() 
```Python 
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}
print(a['two']) # 3.14

# доступ через метод get:
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}

print(a.get('two'))
print(a.get('five'))
print(a.get('five', 5))
print(a.get('ten', 8))
```

**методы для словарей**
* `setdefault()` - Возвращает значение и добавляет ключ в словарь(если указать ключ и еще аргумент справа, то если данного ключа нет в словаре, то он будет добавлен в словарь и выведет знач. Иначе если есть в словаре, то просто выведет знач, игнорируя указанный аргуметнт)
```Python
a = {'one': 42, 'two': 3.14, 'four': 4, 'ten': 10}

s = a.setdefault('five')
print(f'{s = }\t{a=}') #s = None	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None}
eggs = a.setdefault('six', 6)
print(f'{eggs = }\t{a=}') #eggs = 6	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
new = a.setdefault('two')
print(f'{new = }\t{a=}') # new = 3.14	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
new_t = a.setdefault('one', 1_000)
print(f'{new_t = }\t{a=}') # new_t = 42	a={'one': 42, 'two': 3.14, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
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
print(f'{spam = }\t{my_dict=}') # spam = 2 my_dict={'one': 1, 'three': 3, 'four': 4, 'ten': 10}
err = my_dict.pop('six') # будет ошибка т.к six не существует в словаре
err = my_dict.pop() # будет ошибка т.к не чего не передаем в .pop()
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
 *  **my_set = {1, 2, 3, 4, 2, 5, 6, 7} - Изменяемое множество**
 * **my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,)) - Неизменяемое множество**

**методы:**
* add() - Добавляет элемент
```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(7)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(9, 10)   
print(my_set) # TypeError: set.add() takes exactly one\
```
* remove() - Удаляет элемент
```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set) # {1, 2, 3, 4, 6, 7}
my_set.remove(10) # KeyError: 10
```
* discard() - Удаляет элемент
```Python
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set) # {1, 2, 3, 4, 6, 7}
my_set.discard(10)
print((my_set)) #{1, 2, 3, 4, 6, 7} ошибки нет
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
print(42 in my_set) # False
print(5 in my_set) # True
```

## Байты, bytes и bytearray
```Python
text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res)) # b'Hello world!' <class 'bytes'>

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res)) # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!' <class 'bytes'>

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8') # 
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(x) # b'\xd0\x9f\xd1\x80\xd0\xb8'
print(y) # bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')                
```
