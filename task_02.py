"""

В этом задании вы будете реализовывать builtin примитив enumerate
Посмотрите, что эта функция делает

"""


QUESTIONS = []


class enumerate__iter_next:
    """Напишите enumerate, не используя генераторы"""

    def __init__(self, iterable, start=0):
        ...

    def __iter__(self):
        ...

    def __next__(self):
        ...


class enumerate__iter_generator:
    """Напишите enumerate, через класс и используя генератор для __iter__

    Реализуйте решение так, чтобы объект хранил состояние итерации, т.е.

    enumerator = enumerate__iter_generator('abcd')
    for _ in enumerator:
        break

    for _ in enumerator:  # начинает итерации со второй буквы, т.е. 'b'
        ...
    """

    def __init__(self, iterable, start=0):
        ...

    def __iter__(self):
        ...


QUESTIONS.append(
    """
    Какие вещи потребовалось сделать, чтобы передать
    состояние итерации в генератор?
    """
)


def enumerate__generator(iterable, start=0):
    """Напишите enumerate через генераторную функцию"""

    ...


QUESTIONS.append(
    """
    Есть ли какое-то различие в семантике напиcанных примитивов?
    """
)
