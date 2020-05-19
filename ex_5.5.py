with open('05.txt', 'w') as f:
    f.write(input('Введите числа через пробел: '))
j = 0
with open('05.txt') as f:
    for i in f.read().split(' '):
        j += int(i)
print('Сумма чисел: {}'.format(j))
