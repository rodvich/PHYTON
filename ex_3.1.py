def my_divide(num1, num2):
    return num1/num2


lim = float(input('Введите делимое: '))
lit = float(input('Введите делитель: '))
if lit != 0:
    res = my_divide(lim, lit)
    print('Частное равно: ', '{:.2}'.format(res))
else:
    print('Ошибка: "Деление на 0 не выполняется"')