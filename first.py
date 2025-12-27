from visitor import Visitor


class First:
    """
    First, Second - классы с которыми будет работать класс Visitor
    Доступ осуществляется через функцию accept
    Функция принимает на вход класс посетителя, возвращает результат функции посетителя
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def accept(self, visitor: Visitor):
        return visitor.visit_first(self)