class Student:
    def __init__(self, name, surname, age, speciality):
        self.name = name
        self.surname = surname
        self.age = 0
        self.speciality = speciality
    def print_information(self):
        print('Имя - фамилия: ', self.name, ' ', self.surname, ', возраст ', self.age,' лет, специальность ', self.speciality)