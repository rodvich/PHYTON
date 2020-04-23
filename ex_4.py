n = int(input('Введите число: '))
i = 0

while n != 0:
    a = n % 10
    n = (n - a) / 10
    if a >= i:
        i = a

print('Самая большая цифра в числе: ', int(i))
