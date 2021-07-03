"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
lst = [i ** 2 for i in range(1000)]
dct = {i: i ** 2 for i in range(1000)}


def timing(func):
    """Принимает на вход функцию, возвращает разницу между отсечками времени конца и начала"""
    def t(*args):
        import time
        start = time.perf_counter()
        func(*args)
        finish = time.perf_counter()
        r = finish - start
        return r

    return t


@timing
def fill_list(n):
    return [i ** 2 for i in range(n)]


@timing
def fill_dict(n):
    return {i: i ** 2 for i in range(n)}


@timing
def insert_in_list(val, lst):
    idx = int(len(lst) / 2)
    lst.insert(idx, val)


@timing
def get_from_lst(idx, lst):
    lst.pop(idx)


@timing
def delete_from_list(lst):
    idx = int(len(lst) / 2)
    del lst[idx]


@timing
def insert_in_dict(key, val, dct):
    dct[key] = val


@timing
def get_from_dct(key, dct):
    return dct[key]


@timing
def delete_from_dict(key, dct):
    del dct[key]


print(fill_list(1000))
print(fill_dict(1000))
print(insert_in_list(333, lst))
print(get_from_lst(100, lst))
print(delete_from_list(lst))
print(insert_in_dict(6, 15, dct))
print(get_from_dct(6, dct))
print(delete_from_dict(6, dct))
