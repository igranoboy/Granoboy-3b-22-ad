class Car:
    def __init__(self, brand, model, manufacture_year, price):
        self.brand = brand
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price

    def print_information (self):
        print('Марка - модель: ',self.brand,' ', self.model,', год выпуска ', self.manufacture_year, ', цена ', self.price)