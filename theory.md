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




