try:
    with open(test.txt) as file:
        file.write('Hello, world!')
except:
    print('Ошибка')