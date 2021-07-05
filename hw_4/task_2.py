"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""Результат:
Не оптимизированная функция recursive_reverse
0.0536751
0.057045700000000005
0.0643438
Оптимизированная функция recursive_reverse_mem
0.0023785999999999807
0.004989900000000019
0.005299999999999999
Результат выполнения кода с декоратором в разы быстрее, 
причем не отличается для чисел с разным количеством разрядов, в отличие от 
немемоизированной функции. Секрет кажущейся оптимизации в том, что вычисления 
производятся в декораторе, а не в функции. Декоратор создает словарь, где ключ - число,
значение - перевернутое число и выводит значение по ключу. 
То есть, timeit для "оптимизированной" ф-ции замеряет, в сущности, только время вывода значения по ключу словаря. 
Поэтому время и не отличается для чисел разной разрядности.
Мемоизация в данной задаче и будет работать таким образом, запоминая для каждого
вновь поданного на вход числа его перевернутое значение. Для вычисления числа,
мемоизация, пожалуй, не имеет смысла. Типовые ситуации применения мемоизации - в случае 
частых обращений к ограниченному перечню ресурсов, или еще в случае, если мы обращаемся
к предыдущему значению на каждой итерации, чтобы не вы числять его по два раза. 
Вычисление числа, которое может быть любым, к задаче для мемоизации не подходит."""