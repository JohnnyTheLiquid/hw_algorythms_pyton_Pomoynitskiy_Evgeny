"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

import timeit  # импорты в начале файла согласно стандарту
import random

nums_lst = [random.randint(10, 300) for i in range(20)]  # создаем массив случайных целых чисел


def func_1(nums):
    """Сложность ~2 * O(n),
при каждой итерации выполняется действие с двумя массивами
- входным и создаваемым. Создаваемый массив сначала полностью наполняется,
а затем выводится"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """Оптимизированный вариант. Сложность O(n) - один раз пробегается по входному массиву,
    вывод строится на лету"""
    return [el for el in nums if el % 2 == 0]


print(timeit.timeit(stmt='func_1(nums_lst)', setup='from __main__ import func_1, nums_lst'))
print(timeit.timeit(stmt='func_2(nums_lst)', setup='from __main__ import func_2, nums_lst'))

"""Результат вывода
2.8362376
1.5866061999999999
Как мы знаем, comprehensions подобно встроенным ф-циям выполняется быстрее,
чем цикл. Также, если в цикле можно избежать создвания новой локальной 
структуры данных и наполнять ее, лучше избежать"""
