i = 0
j = 0
lines = open('02.txt').readlines()
for line in lines:
    i += 1
    j = 0
    for a in line.split(' '):
        j += 1
    print('{} строка - слов: {}'.format(i,j))
print('\nВсего строк:', i)
