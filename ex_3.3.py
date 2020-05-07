def my_func(num1, num2, num3):
    a = num1 + num2 if num1 + num2 > num2 + num3 else num2 + num3
    a = num1 + num3 if a <= num1 + num3 else a
    return a


n = int(input('1-е число: '))
u = int(input('2-е число: '))
m = int(input('3-е число: '))
print('Сумма двух наибольших аргументов: ', my_func(n, u, m))
