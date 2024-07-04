from abc import ABC, abstractmethod
from pizza_fc import Margherita,Montanara,Carbonara
from Pizza_b import PizzaB


class PizzaFactory(ABC):
    """Класс пицца-фабрика реализация паттерна"""

    @abstractmethod
    def create_pizza(self):
        pass


class MargheritaFactory(PizzaFactory):
    """Абстрактный класс пиццы"""

    def create_pizza(self):
        return Margherita()


class CarbonaraFactory(PizzaFactory):
    """Абстрактный класс пиццы"""

    def create_pizza(self):
        return Carbonara()


class MontanaraFactory(PizzaFactory):
    """Абстрактный класс пиццы"""

    def create_pizza(self):
        return Montanara()

class PizzaBuilder(ABC):
    """Абстрактный класс пиццы"""

    @abstractmethod
    def set_type(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_filling(self):
        pass

    @abstractmethod
    def set_additives(self):
        pass

    @abstractmethod
    def get_pasta(self):
        pass
class OnePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = PizzaB()

    def set_type(self):
        self.pizza.type = "4 сыра"

    def set_sauce(self):
        self.pizza.sauce = "Сырный"

    def set_filling(self):
        self.pizza.filling = "Самый вкусный"

    def set_additives(self):
        self.pizza.additives = ["Оливки", "Маслины"]

    def get_pasta(self):
        return self.pizza


class TwoPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = PizzaB()

    def set_type(self):
        self.pizza.type = "Классическая"

    def set_sauce(self):
        self.pizza.sauce = "Томатный"

    def set_filling(self):
        self.pizza.filling = "Курица"

    def set_additives(self):
        self.pizza.additives = ["Ананас", "Маслины"]

    def get_pasta(self):
        return self.pizza




