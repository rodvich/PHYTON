def fact(number):
    num = 1
    while num <= number:
        yield num
        num += 1


res = 1
n = int(input('Получить факториал числа: '))
for el in fact(n):
    res *= el
print('факториал числа {} = {}'.format(n, res))
