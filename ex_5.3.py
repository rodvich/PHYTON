workers = []
i = j = 0
lines = open('03.txt').readlines()
for line in lines:
    a, b = line.split(' ')
    i += float(b)
    j += 1
    if float(b) < 20000:
        workers.append(a)
print('Сотрудники получающие меньше 20 000: ', workers)
print('Средняя величина дохода сотрудников: ', i/j)
