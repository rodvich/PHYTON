my_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
print('Исходный список:', my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print('Результат:', new_list)
