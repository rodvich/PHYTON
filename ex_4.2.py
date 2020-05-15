my_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
print('Исходный список:', my_list)
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i-1] < my_list[i]]
print('Результат:', new_list)
