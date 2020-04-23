s = int(input('Количество секунд = '))

m = s // 60
s = s % 60
h = m // 60
m = m % 60

print('{:02}:{:02}:{:02}'.format(h, m, s))
