def sum_func():
    my_sum = 0
    j = 0
    while j != 'stop':
        my_str = input('Введите строку чисел, для завершения введите "q": ')
        a = my_str.split(' ')
        for i in a:
            if i != 'q':
                my_sum = my_sum + int(i)
            else:
                j = 'stop'
                break
        print(my_sum)


sum_func()