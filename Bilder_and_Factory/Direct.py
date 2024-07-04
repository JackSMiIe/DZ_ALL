from Bilder_and_Factory import MontanaraFactory, CarbonaraFactory, MargheritaFactory,OnePizzaBuilder,TwoPizzaBuilder



class PizzaClient:
    def __init__(self, factory_bilder):
        self.factory_bilder = factory_bilder

    def prepare_pizza(self):
        pizza = self.factory_bilder.create_pizza()
        print(f"Сейчас мы приготовим {pizza.get_type()} с {pizza.get_sauce()}")
        print(f"Добавим в нее {', '.join(pizza.get_additives())}")
        print(f"А в качестве начинки положим {pizza.get_filling()}")

        return pizza

    def construct_pizza(self):
        self.factory_bilder.set_type()
        self.factory_bilder.set_sauce()
        self.factory_bilder.set_filling()
        self.factory_bilder.set_additives()
        return self.factory_bilder.get_pasta()

if __name__ == "__main__":
    Margherita_for_vasya = PizzaClient(MargheritaFactory())
    Carbonara_for_petya = PizzaClient(CarbonaraFactory())
    Montanara_for_vova = PizzaClient(MontanaraFactory())

    # new_pizza = SpaghettiBuilder()


    print("ГОТОВИМ ДЛЯ ВАСИ")
    Margherita_for_vasya.prepare_pizza()
    print("-----------------")
    print("ГОТОВИМ ДЛЯ ПЕТИ")
    Carbonara_for_petya.prepare_pizza()
    print("-----------------")
    print("ГОТОВИМ ДЛЯ ВОВЫ")
    Montanara_for_vova.prepare_pizza()
    print(100 * '-')
    """Пицца конструктор"""
    print("ГОТОВИМ ДЛЯ КОСТИ")
    pizza_builder = OnePizzaBuilder()
    pizza_director = PizzaClient(pizza_builder)
    pizza = pizza_director.construct_pizza()
    print(pizza)



