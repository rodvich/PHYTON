from itertools import count, cycle


def my_count_func(start_num, stop_num):
    for i in count(start_num):
        if i > stop_num:
            break
        else:
            print(i)


def my_cycle_func(my_list, iterat):
    i = 0
    it = cycle(my_list)
    while i < iterat:
        print(next(it))
        i += 1


my_count_func(int(input("Начальное число: ")), int(input("Конечное число: ")))
my_cycle_func([1, 0], int(input("Повторение элементов списка [1, 0]: ")))
