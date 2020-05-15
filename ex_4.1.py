def my_func(tim, mon, bon):
    return tim * mon + bon


print('З/П: ', my_func(float(input('Выработка в часах: ')), float(input('Ставка в час: ')), float(input('Премия: '))))
