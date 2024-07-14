
class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def get_info(self):
        return {
            'Type': self.shoe_type,
            'Style': self.shoe_style,
            'Color': self.color,
            'Price': self.price,
            'Manufacturer': self.manufacturer,
            'Size': self.size
        }


# Представление (View)
class ShoeView:
    def display_shoe(self, shoe):
        print("Shoe Information:")
        print(f"Type: {shoe['Type']}")
        print(f"Style: {shoe['Style']}")
        print(f"Color: {shoe['Color']}")
        print(f"Price: {shoe['Price']}")
        print(f"Manufacturer: {shoe['Manufacturer']}")
        print(f"Size: {shoe['Size']}")


# Контроллер (Controller)
class ShoeController:
    def __init__(self, shoe):
        self.shoe = shoe
        self.view = ShoeView()

    def show_shoe(self):
        shoe_info = self.shoe.get_info()
        self.view.display_shoe(shoe_info)


# Пример использования MVC для класса Shoe
shoe_data = {
    'shoe_type': 'мужская',
    'shoe_style': 'кроссовки',
    'color': 'черный',
    'price': 99.99,
    'manufacturer': 'Nike',
    'size': 42
}

shoe_model = Shoe(shoe_data['shoe_type'], shoe_data['shoe_style'], shoe_data['color'],
                  shoe_data['price'], shoe_data['manufacturer'], shoe_data['size'])

shoe_controller = ShoeController(shoe_model)
shoe_controller.show_shoe()
