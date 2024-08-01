import json


class Pizza:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = []
        self.toppings_price = 0

    def add_topping(self, topping, price):
        self.toppings.append(topping)
        self.toppings_price += price

    def get_price(self):
        return self.base_price + self.toppings_price

    def get_description(self):
        return f"{self.name} с топингами: {', '.join(self.toppings)}"


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.get_price() for pizza in self.pizzas)

    def save_to_file(self, filename):
        order_details = {
            "pizzas": [
                {
                    "Описание": pizza.get_description(),
                    "Цена": pizza.get_price()
                } for pizza in self.pizzas
            ],
            "Итог": self.calculate_total()
        }
        with open(filename, 'w') as file:
            json.dump(order_details, file, indent=4)


class Pizzeria:
    def __init__(self):
        self.menu = [
            Pizza("Margherita", 5),
            Pizza("Pepperoni", 6),
            Pizza("BBQ Chicken", 7),
            Pizza("Hawaiian", 6),
            Pizza("Veggie", 5)
        ]
        self.toppings = {
            "Sweet Onion": 0.5,
            "Jalapeno": 0.5,
            "Chili": 0.5,
            "Pickle": 0.5,
            "Olives": 0.5,
            "Prosciutto": 1.0
        }
        self.orders = []
        self.total_revenue = 0

    def create_order_example(self):
        order = Order()

        # Пример выбора пиццы и добавления топпингов
        selected_pizza = self.menu[0]  # Маргарита
        pizza = Pizza(selected_pizza.name, selected_pizza.base_price)
        pizza.add_topping("Olives", self.toppings["Olives"])
        pizza.add_topping("Prosciutto", self.toppings["Prosciutto"])
        order.add_pizza(pizza)

        return order

    def process_payment_example(self, order, payment_method):
        total = order.calculate_total()
        if payment_method == "cash":
            print(f"Пожалуйста заплатите ${total} наличными.")
        elif payment_method == "card":
            print(f"${total} будет списано с карты.")
        self.total_revenue += total
        self.orders.append(order)

    def view_statistics_example(self):
        total_pizzas = sum(len(order.pizzas) for order in self.orders)
        print(f"Всего продано пицц: {total_pizzas}")
        print(f"Доход: ${self.total_revenue}")


def main():
    pizzeria = Pizzeria()

    # Пример создания заказа
    order = pizzeria.create_order_example()

    # Пример обработки платежа
    pizzeria.process_payment_example(order, "card")

    # Сохранение заказа в файл
    order.save_to_file("order.json")

    # Пример просмотра статистики
    pizzeria.view_statistics_example()


if __name__ == "__main__":
    main()
