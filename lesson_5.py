# Как читать открытый файл
# f = open('README.md')#.read()
# # text = f.read()
# lines = f.readlines()
# for line in lines:
#     # print(line, end='')
#     print(line.strip())
# print(f.readline())
# print(f.readline())

# Как записывать в файл

# r - открыть на чтение
# w - затирает существующий файл
# x - не затирает существующий файл
# a - добавить информацию в конец файла
#
# b - открыть в двоичном формате
# t - открыть в текстовом формате
#
# + - открыть файл на чтение и запись

# f = open('README.md', 'w')
# f.write('FAT\nASS')
# # data = ['qwe', 'asd', 'zxc']
# # f.write('\n'.join(data))
# # f.writelines(data)
# f.close()

# f = open('000.txt', 'w')    # , encoding='utf-8')
# # f.write('qweqwe\nassass')
# # f.close()
# # print('123123')
# print('123123', file=f)

# # Конструкция не требующая написания закрытия
# with open('README.md', 'w') as f:
#     f.write('FAT\nASS')
# #     print(f.closed)
# #
# # print(f.closed)
# # print(f.mode)
# # print(f.name)
# # r'Makcintosh HD\Пользователи\user\Рабочий стол\PHYTON\README.md'

# with open('11.txt', 'w+') as f:
#     # print(f.tell())
#     f.write('qwe\nasd\nzxc')
#     # print(f.tell())
#     f.seek(0)
#     text = f.read()
#     print(text)

# import os
# # os.rename('11.txt', '22.txt')
# os.remove('22.txt')
# print(os.path.exists('README.md'))

# import json
#
# data = {'income': {'salary': [50000, 1000], 'bonus': 10000}}
# # with open('Ivan.json', 'w') as f:
# #     json.dump(data, f)
# #
# # with open('Ivan.json') as f:
# #     js = json.load(f)
# # print(js)
#
# a = json.dumps(data)
# print(type(a))
# print(json.loads(a))
#
# # import os
# # os.remove('Ivan.json')

# import shutil
# shutil.copyfile('откуда', 'куда')   # тянет метаданные
# shutil.copy('откуда', 'куда')
# shutil.rmtree('')
# shutil.move('откуда', 'куда')
