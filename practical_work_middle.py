# Написать программу, которая принимает на вход две строки и выводит их пересечение (т.е. символы, встречающиеся в обеих строках).

str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')
intersection = []

for sign in str_1:
    try:
        str_2.index(sign)
        intersection.append(sign)
    except ValueError:
        continue

print(intersection)