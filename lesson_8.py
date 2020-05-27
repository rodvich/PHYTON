# class DataBaseConnection:
#     def connect(self):
#         print('connecting')
#
#     @staticmethod   # отдельный метод - не требует обращения в инит
#     def select(ip):
#         print(f'selecting {ip=} ')
#
#
# db = DataBaseConnection()
# db.select('10.116.121.21')
#
# DataBaseConnection.select('10.116.121.21')


# class MyClass:
#     @classmethod    # отдельный метод, можно взаимодействовать с другими частями класса
#     def my_method(cls, param):
#         print(cls, param)
#
#
# MyClass.my_method('qwe')

# class Customer:
#     """ Это класс Customer"""
#
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# john = Customer('John', 985659595)

# print(john.__dict__)
# print(john.__doc__)
# a = list()
# print(a.__doc__)

# print(john.__class__.__name__)
# print(john.__module__)

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return self.name + ' ' + self.surname
#
#
# class Teacher(Person):
#     def to_teach(self, subj, *pupils):
#         for pupil in pupils:
#             pupil.to_take(subj)
#
#
# class Pupil(Person):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledges = []
#
#     def to_take(self, subj):
#         self.knowledges.append(subj)
#
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = list(subjects)
#
#     def my_list(self):
#         return self.subjects
#
#
# s = Subject('math', 'physics', 'biology')
# t = Teacher('Ivan', 'Ivanov')
# print(t)
# p_1 = Pupil('Petr', 'Petrov')
# p_2 = Pupil('Sidr', 'Sidorov')
# p_3 = Pupil('Oleg', 'Olegov')
# print(p_1, p_2, p_3)
#
# t.to_teach((s, p_1, p_2))
# print(p_1.knowledges[0].my_list())
# print(p_2.knowledges[0].my_list())
# print(p_3.knowledges)


# class MyOwnException(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# inp_data = int(input('Введите положительное число'))
#
# try:
#     if inp_data < 0:
#         raise MyOwnException('Вы ввели отрицательное число')
# except MyOwnException as err:
#     print(err)
#
# class MyDict(dict):
#     pass

# import math

# import numpy
# print(numpy.array(2))

# import psutil
# print(psutil.cpu_stats())
# # print(psutil.disk_usage('c:'))
# print(psutil.virtual_memory())

# import requests
# response = requests.get('https://www.bbc.com/')
# print(response.content)

# LotoCard LotoGame
