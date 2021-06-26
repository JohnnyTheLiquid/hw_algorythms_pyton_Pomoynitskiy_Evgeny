"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# берем за основу пример с урока


class TaskBoard:
    def __init__(self):
        self.elems = []
        self.solved = []
        self.to_redo = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def solve(self):
        return self.solved.insert(0, self.elems.pop())

    def redo(self):
        return self.to_redo.insert(0, self.elems.pop())

    def size(self):
        return len(self.elems)

    def task_list(self):
        return self.elems


if __name__ == '__main__':
    tsk_obj = TaskBoard()
    print (tsk_obj.is_empty())

    tsk_obj.to_queue('task1')
    tsk_obj.to_queue('task2')
    tsk_obj.to_queue('task3')
    print(tsk_obj.size())
    print(tsk_obj.task_list())

    tsk_obj.solve()
    tsk_obj.redo()
    print(tsk_obj.elems)
    print(tsk_obj.to_redo)



