class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = 0

    def print_information(self):
        print('Имя: ', self.name, ', порода: ', self.breed, ', возраст: ', self.age)