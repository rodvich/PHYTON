from googletrans import Translator
lines = open('04.txt').readlines()
f = open('04+.txt', 'w+')
for line in lines:
    a, b = line.split(' — ')
    a = Translator().translate(a, dest='ru')
    f.write('{} — {}'.format(str(a.text).capitalize(), b))
f.close()
