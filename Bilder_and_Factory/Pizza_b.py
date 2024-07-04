class PizzaB:
    """Класс пицца-строитель реализация паттерна"""

    def __init__(self, type=None, sauce=None, filling=None, additives=None):
        self.type = type
        self.sauce = sauce
        self.filling = filling
        self.additives = additives

    def __str__(self):
        return (f"Тип пиццы: {self.type}\n"
                f"Соус: {self.sauce}\n"
                f"Топинг: {self.filling}\n"
                f"Добавки: {', '.join(self.additives) if self.additives else 'None'}")