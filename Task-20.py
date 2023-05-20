import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 101))
print('Массив: ', my_list)

maximum = my_list[0]
for i in range(9):
    if maximum < my_list[i + 1]:
        maximum = my_list[i + 1]
print('Максимальное значение: ', maximum)

minimum = my_list[0]
for i in range(9):
    if minimum > my_list[i + 1]:
        minimum = my_list[i + 1]
print('Минимальное значение: ', minimum)