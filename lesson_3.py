# print(max(2, 3, 4, 5))
# print(max('zz', 'aaa'))
# print(max('zz', 'aaa', key=len))
# print(max('zzdgdgfdgff', 'ajgfnjdnjaa', key=len))
# print(round(1.985432, 2))

# def say_hello(name, surname):
#     print('Hello!', name, surname)
#
# say_hello('Ivan', 'Ivanov')
# say_hello('Artem', 'Artemov')

# def average(numbers):
#     answer = (sum(numbers) / len(numbers))
#     return answer
#
# averenge_of_numbers
#
# out = average([1, 2, 3, 4, 5, 6, 7, 8])
# print(out)

# def print(text): #- нельзя
#     i = 0
#
# print('q')


# def test(x):
#     # global x
#     return x - 1
#
#
# x = 100
# x = test(x)
# print(x)

# def my_func(name, surname=''):
#     print(name, surname)
#
# my_func('Ivan')
# my_func('Ivan', 'Ivanov')

# def my_func(name, *args):
#     print(name, args)
#
# my_func('ivan', 200)
# my_func('ivan', 200, 300, 500)

# def my_func(name, surname, age):
#     print(name, surname, age)
#
# my_func(10, 'Ivan', 'Ivanov')
# my_func(age=10, name='Ivan', surname='Ivanov')

# def my_func(**kwargs):
#     print(kwargs)
#
# my_func(age=10, name='Ivan', surname='Ivanov')

# names = ['Aleksandra', 'Max', 'Artem']
# ages = [25, 38, 85]
# for name, age in zip(names,ages):
#     print(name, age)
#
# print(list(zip(names, ages)))
# print(dict(zip(names, ages)))

# ages = [25, 38, 85]
# for i in ages:
#     print(i)

# def my_pow(x):
#     return x**2

# def my_filter(x):
#     return x > 0
#
# data = [-2, -10, 5, 9]
# result = []
# for i in data:
#     result.append(my_pow(i))
# print(result)

# result = list(map(my_pow, data))
# result = list(filter(my_filter, data))
# print(result)

# result = list(map(lambda qwe: qwe**2, data))
# result = list(filter(lambda x: x > 0, data))
# print(result)

# for i in range(1, 10, 3):
#     print(i, 'Hello')

# for i in range(1, 10, 3):
#     print('Hello', i)
#
# a = ['name', 'surname', 'log']
# name, surname, _ = a
# print(name, surname)

# def my_func(name, surname):
#     """
#     :param name:
#     :param surname:
#     :return:
#     """
#
# str()

# def my_func(a, b):
#     return a / b

# one, two, *args = ['qwe', 'asd', 'zxc', 'asd', 1 , 2, 3][:2]
# print(one, two)

