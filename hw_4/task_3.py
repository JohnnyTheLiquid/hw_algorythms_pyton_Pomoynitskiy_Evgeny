"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    """Предложенный вариант. Переводим число в строку, из нее делаем список,
    к списку применяем встроенные ф-ции reverse() и join()
    Встроенное - значит достаточно быстрое """
    lst = list(str(enter_num))  # O(len(enter_num)) ~O(const) ~O(1) согласно таблице
    lst.reverse()  # O(len(enter_num)) согласно таблице, пропорционально количеству разрядов числа ~O(const) ~O(1)
    return int(''.join(lst))  # O(len(enter_num)) - пропорционально количеству разрядов числа ~O(const) ~O(1)


def main():
    num = 123456789
    for i in range(1000000):
        revers_1(num)
        revers_2(num)
        revers_3(num)
        revers_4(num)


for i in range(1, 5):
    print(timeit.timeit(stmt=f'revers_{i}(123456789)', setup=f'from __main__ import revers_{i}'))

run('main()')

"""Результат исполнения
3.0686787
2.0119763
0.4177800999999999
0.9662406999999993
         15000004 function calls (6000004 primitive calls) in 10.788 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.788   10.788 <string>:1(<module>)
10000000/1000000    5.287    0.000    5.287    0.000 task_3.py:21(revers_1)
  1000000    2.145    0.000    2.145    0.000 task_3.py:31(revers_2)
  1000000    0.552    0.000    0.552    0.000 task_3.py:39(revers_3)
  1000000    1.208    0.000    1.571    0.000 task_3.py:45(revers_4)
        1    1.232    1.232   10.788   10.788 task_3.py:54(main)
        1    0.000    0.000   10.788   10.788 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.232    0.000    0.232    0.000 {method 'join' of 'str' objects}
  1000000    0.131    0.000    0.131    0.000 {method 'reverse' of 'list' objects}

Результаты изменения с помощью timeit и CProfile сопоставимые, 
рейтинг скорости одинаковый, хотя в абсолютных значениях отличаются. При том,
что количество запусков 1 млн и там и там, способ запуска отличается (цикл и
встроенное в метод значение переменной) полагаю, это влияет на расчет значения"""

"""revers_1 самая медленная, поскольу рекуррентная. В общем случае сложность O(2^n), 
экспоненциально (по основанию 2) зависит от количества разрядов числа. 
revers_2 более быстрая, делает те же вычисления, что рекуррентная, но в цикле. Сложность O(n)
Это быстрее. 
revers_3 очень быстрая, через срезы, сложность O(количество разрядов в числе), 
то есть, O(const) ~ O(1)
revers_4 медленнее, чем срезы, но тоже достаточно быстрая по сравнению с 
математическими вычислениями за счет применения встроенных функций итоговая
сложность O(const) ~ O(1), только здесь больше операций с константной сложностью, чем в 3"""