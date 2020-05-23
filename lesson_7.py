# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fc = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#         # return self
#
#     def __str__(self):
#         return ', '.join(self.modules)
#
#     def __del__(self):
#         print('объект удален')
#
#     def __setattr__(self, key, value):
#         # super().__setattr__(key, value)
#         self.__dict__[key] = value
#         print(f'Добавлено {key}: {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price=None):
#         print(f'Машина {self.modules}, модули: {self.modules}, цена: {price}')
#
#     def __eq__(self, other):
#         return self.fc == other


# car = Car()
#
# person_want = 'теплый руль'
# # car.modules.append(person_want)
# car + person_want   # + person_want
#
# person_want = 'подогрев сидений'
# # car.modules.append(person_want)
# car + person_want
#
# car.module = 'Tesla'
# # print(car.modules)
# print(car.module)
# print(car[0])   # car.__getitem__(1)
#
# # car()
# # car(price=5000)
# print(car == 10)
# print(car == 7)


# from abc import ABC, abstractmethod
#
# class MyAbsClass(ABC):
#     @abstractmethod     # обязует использовать функцию
#     def my_method1(self):
#         print('Тут будет считывание')
#         pass
#
#     @abstractmethod
#     def my_method2(self):
#         pass
#
#
# class MyClass(MyAbsClass):
#     def my_method1(self):
#         pass
#
#     def my_method2(self):
#         pass
#
#     def qwe(self):
#         pass
#
#
# mc = MyClass()

# a = [1, 1, 3, 4, 5, 5, 7]
# for i in a: # __iter__? -> object -> __next__ -> StopIteration
#     print(i)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             self.i = 0
#             raise StopIteration
#
#
# qwe = Iterator()
# for i in qwe:
#     print(i)
# for i in qwe:
#     print(i)

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         #if self.age ->
#         return self._age
#
# # lot of code
#
#
# human = Human('alex', 10)
# print(human.name)
# print(human.age)


# class WinDoor:
#     def __init__(self, w, h):
#         self.square = w * h
#
#
# class Room:
#     def __init__(self, len1, len2, h):
#         self.square = 2 * h * (len1 + len2)
#         self.wd = []
#
#     def add_windoor(self, w, h):
#         self.wd.append(WinDoor(w, h))
#
#     def common_square(self):
#         main_square = self.square
#         for el in self.wd:
#             main_square -= el.square
#         return main_square
#
#
# r = Room(7, 6, 3.7)
# print(r.square)
# r.add_windoor(2, 2)
# r.add_windoor(2, 1)
#
# print(r.common_square())
