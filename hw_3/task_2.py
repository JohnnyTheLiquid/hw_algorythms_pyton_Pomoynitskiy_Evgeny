"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import uuid as u
import hashlib as h
import csv

salt = u.uuid3(u.NAMESPACE_DNS, 'salt').hex  # если использовать uuid4 то каждый раз генерируется новое число,
# что делает невозможной проверку загруженных из файла хэшей

with open('passwords.txt', 'w', newline='') as f:  # заполним файл ранее сфоримрованным хэшем пароля
    writer = csv.writer(f, delimiter=',')
    writer.writerow([h.sha256('password_1'.encode() + salt.encode()).hexdigest()])


def check_pwd():
    pwd = input('Enter your password ')
    with open('passwords.txt', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([h.sha256(pwd.encode() + salt.encode()).hexdigest()])

    pwd_check = input('Enter your password again ')
    with open('passwords.txt', 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        if list(reader)[-1][0] == h.sha256(pwd_check.encode() + salt.encode()).hexdigest():
            return "Success"
        else:
            return "Passwords don't match"


print(check_pwd())
