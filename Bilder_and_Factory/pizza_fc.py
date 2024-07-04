from abc import ABC, abstractmethod



class Pizza(ABC):
    """Класс пицца"""

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass


class Margherita(Pizza):
    def get_type(self):
        return "Margherita"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Сыр", "Чеснок"]


class Carbonara(Pizza):
    def get_type(self):
        return "Carbonara"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Пармезан", "Петрушка"]


class Montanara(Pizza):
    def get_type(self):
        return "Montanara"

    def get_sauce(self):
        return "Песто соус"

    def get_filling(self):
        return "Мясо"

    def get_additives(self):
        return ["Анчоусы", "Томаты"]






