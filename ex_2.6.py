products = []
n = 0
while input("Добавить продукт да/нет? ") == 'да':
    n = n + 1
    charact = {}
    charact['название:'] = input("Название: ")
    charact['цена:'] = input("Цена: ")
    charact['количество:'] = input("Количество: ")
    charact['ед:'] = input("Единицы: ")
    products.append(tuple([n, charact]))
print(products)
analitics = {}
for product in products:
    for key, value in product[1].items():
        if key in analitics:
            analitics[key].append(value)
        else:
            analitics[key] = [value]
print(analitics)