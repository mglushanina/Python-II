"""

Напишите класс, который считает элементы из итерабла.
Считаем, что все они могут быть положены в словарь

Бонус, если унаследуетесь от словаря

Эту задачу будем обсуждать на разборе

"""


class MyCounter:
    def __init__(self, iterable=None):
        ...

    def extend(self, iterable):
        ...

    def get_stats(self):  # получить словарь со счетчиками
        ...


# # from collections import Counter
# c = MyCounter('abcdef')
# c.extend('abc')
# c.get_stats()  # {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1}
