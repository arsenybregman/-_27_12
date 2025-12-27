from first import First
from second import Second
from visitor_minus import VisitorMinus
from visitor_sum import VisitorSum

if __name__=='__main__':
    # Создаем объекты классов
    obj_first = First(10, 5)
    obj_second = Second(10, 5, 0.7)

    # Создаем посетителей
    sum_visitor = VisitorSum()
    minus_visitor = VisitorMinus()

    # Вызываем функцию accept и передаем в нее посетителя
    print(obj_first.accept(sum_visitor))
    print(obj_second.accept(sum_visitor))
    print(obj_first.accept(minus_visitor))
    print(obj_second.accept(minus_visitor))