try:
    with open(input('Введите имя файла: ')) as file:
        content = file.read()
        print(content)
        file.close()
except:
    print('Ошибка')