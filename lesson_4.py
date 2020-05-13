# import lesson_3 as lib
# lib.test(10)

# import lesson_3
# lesson_3.test(10)

# from lesson_3 import *

# import phyton.lesson_3 as lib

# print(__name__)
# if __name__ == '__main__':
#     # my_func(1,2)
#     print('qwe qwe qwe')

# import time
# a = time.time()
# for i in range(10000000):
#     pass
# b = time.time()
# print(b-a)
# print(time.localtime())

# import math
# print(math.pi)
#
# a = 5.98
# print(math.floor(a))
# print(math.ceil(a))

# import sys
# sys.path.insert(0, '')
# print(sys.path)
#
# a = mac:\Users\user\Desktop\PHYTON

# from sys import argv
# if 'h' in argv[1:] or 'help' in argv[1:]:
#     print('Описание,как работать со скриптом')
# else:
#     path1, path2 = print[1:]
#     print('Копирую из {path1} в {path2}')

# import os
# os.chdir('C://')
# print(os.getcwd())
# os.remove()
# os.mkdir()
# print(os.listdir())
# for path in os.listdir():
#     print(path, os.path.isdir(path))
# os.system()

# my_list = [0, 1, 2, 3, 5, 6, 7, 8, 9]
# new_list = [el ** 2 for el in my_list] #if el % 2 == 0]
# print(new_list)
#
# new_dict = {el: el ** 2 for el in my_list}
# print(new_dict)
# set = list, но с ()

# import random
# print(random.randint(0, 100))
# print(random.random())
#
# print(random.randrange(10, 20, 2))
# print(random.randrange(10, 20, 3))
# print(random.randrange(10, 20, 5))

# generator = (param * param for param in range(5))
# print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# for i in generator:
#     print(i)
# for i in generator:
#     print(i)

# def generator():
#     while True:
#         yield 100
#         # yield open('')
#     # for el in (10, 20, 30):
#     #     yield el
#
# g = generator()
# print(g)
# for i in g:
#     print(i)
#
# g = generator()
# for i in g:
#     print(i)

# from functools import reduce, partial
# # def my_f(num1, num2):
# #     return num1 + num2
# # print(reduce(my_f, [10, 20 , 30, 5]))
#
# def my(p1, p2):
#     return p1 * p2
# new_f = partial(my, 2)
# print(new_f)
# print(new_f(4))

import itertools

# for i in itertools.count(start=0, step=1):
#     if i == 15:
#         break
#     print(i)

# from itertools import cycle
# c = 0
# for i in cycle(['зеленый', 'желтый', 'красный']):
#     print(i)
#     c += 1
#     if c > 10:
#         break
#