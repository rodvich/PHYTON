def my_func(x, y):
    a = 1
    while y != 0:
        a = a * x
        y = y + 1
    if a > 0:
        return 1 / a
    else:
        return 0


num = float(input('Введите действительное положительное число: '))
pwr = int(input('Введите целое отрицательное число: '))

if (num >= 0) & (pwr < 0):
    print('При возведении числа {} в степень {}, получим ответ: {}'.format(num, pwr, my_func(num, pwr)))
else:
    print('Введенные числа не соответствуют условиям задачи!')
