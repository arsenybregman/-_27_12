class Visitor:
    """
    Абстрактный класс Visitor от которого будут наследоваться остальные посетители с конкретной реализацией методов
    Доступ осуществляется через функцию accept в классе объекта
    Каждому классу объекта соответствует своя функция: классу First - visit_first, классу Second - visit_second
    """
    def visitor_first(self, first:'First'):
        pass

    def visitor_second(self, second:'Second'):
        pass
