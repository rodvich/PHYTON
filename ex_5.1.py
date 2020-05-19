print('Об окончании ввода данных свидетельствует пустая строка.')
with open('01.txt', 'w+') as f:
    while True:
        t = input('Введите текст: ')
        if t != '':
            f.write('{}\n'.format(t))
        else:
            break
