from first import First
from second import Second
from visitor import Visitor


class VisitorMinus(Visitor):
    """
    Классы Visitor_sum и Visitor_minus - классы реализующие посещения для классов объектов
    Каждому классу объекта соответствует своя функция: классу First - visit_first, классу Second - visit_second
    Получают на вход объект соответствующего класса, считают результат на основании значения его атрибутов
    """
    def visit_first(self, first: First): #
        return first.a - first.b

    def visit_second(self, second: Second):
        return second.a - second.b * second.mn