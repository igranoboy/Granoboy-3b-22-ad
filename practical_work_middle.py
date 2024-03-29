# Написать программу, которая принимает на вход две строки и выводит их пересечение (т.е. символы, встречающиеся в обеих строках).

#объявляем переменные и просим пользователя заполнить их значениями
str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')

#создаем пустой список, в который будем записывать результат
intersection = []

#создаем цикл, который попытается найти каждый символ первой строки во второй строке
for sign in str_1:
    try:
        str_2.index(sign)
        intersection.append(sign) #если найти получится, то добавляем символ в результирующий список
    except ValueError: #если поиск закончился ошибкой, то продолжаем цикл до последнего символа первой строки
        continue

print(intersection)