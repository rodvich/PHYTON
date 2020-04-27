number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'зима',
                  2: 'зима',
                  3: 'весна',
                  4: 'весна',
                  5: 'весна',
                  6: 'лето',
                  7: 'лето',
                  8: 'лето',
                  9: 'осень',
                  10: 'осень',
                  11: 'осень',
                  12: 'зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number - 1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]}")
else:
    print("You made a mistake") 