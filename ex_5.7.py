import json
company = {}
all_bonus = 0
i = 0
with open('07.txt', 'r') as f:
    for line in f:
        name, _, plus, minus = line.split()
        company[name] = int(plus) - int(minus)
        if company[name] >= 0:
            all_bonus = all_bonus + company[name]
            i += 1
    if i != 0:
        mean_bonus = all_bonus / i
        print('Средняя прибыль - {:.0f}'.format(mean_bonus))
    else:
        print('Все работают в убыток')
    all_of_this = [company, {'average_profit': round(mean_bonus)}]
    print('Прибыль каждой компании - {}'.format(all_of_this))
with open('ex_07.json', 'w+') as write_js:
    json.dump(all_of_this, write_js)
    js_str = json.dumps(all_of_this)
    print('Создан файл с расширением json со следующим содержимым:\n{}'.format(js_str))