# модуль
# print(abs(-5))

# умножение в двоичной системе (И)
# print(5 & 3)
# сложение в двоичной системе (ИЛИ)
# print(5 | 3)
# отличные значения в двоичной системе = 1 (исключающее ИЛИ)
# print(5 ^ 3)
# битовый сдвиг вправо (2 встепени 1)
# print(6 >> 1)
# битовый сдвиг влево (2 встепени 6)
# print(6 << 2)
# указать в системе счисления число в 2
# print(int('0111', 2))
# oct двоичные print(bin(17))
# hex шестнадцатеричные print(hex(17))

# my_string = 'Anastasia Ivanova'
# my_email = 'ivan@mail.ru'
# print(my_string[1])
# print(my_string[2:4]) # [start:stop:step]
# print(my_string[::-2])
# print(len(my_string))
# print(my_email.split('@'))  # list - тип данных
# print(my_string.split())
# my_list = ['Anastasia', 'Ivanova', '58']
# print((' '.join(my_list)))
# print(my_string.lower())
# print(my_string.upper())
# print(my_string.capitalize())
# print(my_string.title())
# print(my_string.istitle())
# print('a' in my_string)
# print(my_string.count('Ivanova'))
# print(my_string.find('!', 12))

# my_list = list()
# my_list = []
# a = 'ASDASD'
# my_list = ['qwe', 54, a, 54.6, False]
# my_list[0] = 'zc'
# print(my_list)
# print(my_list[::-1])
# my_list.append('Barney')
# my_list.insert(1, 'Misha')
# print(my_list)
# pop = вырезать
# qwe = my_list.pop()
# print(my_list, qwe)
# my_list.reverse()
# print(my_list)
# print(my_list.count(54))
# print(54 in my_list)

# кортедж (не редактируется / меньше весит)
# a = ('qwe', 54, a, 54.6, False) # tuple
# print(a[1:4])

# my_set = set()
# my_set = {}
# my_set = {1, 5, 2, 2, 2, 3, 4, 1, 6, 7, 2, 2}
# print(my_set)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)
# print(a == b)
# print(a & b)
# print(a - b)
# print(b - a)
# print(a ^ b)
# a = [1, 5, 2, 2, 2, 3, 4, 1, 6, 7, 2, 2]
# print(len(set(a)))
# a.remove(3)   #только имеющиеся числа
# print(a)
# a.discard(5)
# print(a)

# human = dict()    словарь
# human = {'name': 'Maxim', 'age': 95}
# print(human['name'])
# human['data'] = [1, 2, 3, 4]
# print(human)
#
# print(human['name'])
# print(human.get('qwe'))

# human.pop('age')
# print(human)

# print(human.popitem())
# print(human)
# print(human.keys())
# print(human.values())
# print(human.items())

# print(b'text')
# print(bytes('текст'.encode('utf-8')))

# a = [10]
# b = [10]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)

# a = [1, 2, 3, 4, 5]

# a = 1
# try:
#     a = int(input())
#     print(10 / a)
# except ZeroDivisionError:
#     print('деление на ноль!')
# except ValueError:
#     print('Не число')

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)

# human = {'name': 'Maxim', 'age': 95}
# for key, value in human.items():
#     print(key, value)

# if 5 > 6:
#     a = 5
# else:
#     a = 0

# a = 5 if 7 > 6 else 0
# print(a)
# age = int(input('Age: '))
# print('Welcome' if age >= 18 else 'No Access!')

# my_list = [1, 2, 3, 4, 5]
# for num in my_list:
#     my_list.remove(num)
# print(my_list)
#
# my_list = [1, 2, 3, 4, 5]
# for num in my_list[:]:
#     my_list.remove(num)
# print(my_list)
#
# my_list = [1, 2, 3, 4, 5]
# for num in my_list.copy():
#     my_list.remove(num)
# print(my_list)

# import copy
# a = [1, 2, 3, [100, 200]]
# b = copy.deepcopy(a)
# b[3].append(300)
# print(a)