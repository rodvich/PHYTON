import copy
import random


class LotoCard:
    def __init__(self):
        all_col = random.sample(range(1, 91), 15)
        self.card = [sorted(all_col[i:i + 5]) for i in range(0, len(all_col), 5)]
        self.view_card = copy.copy(self.card)
        placeholders = ' '.join(['{:>2}' for i in range(9)])
        for line in self.view_card:
            for space in ' ' * 4:
                line.insert(random.randint(0, len(line) - 1), space)
        self.view_card = [placeholders.format(*line) for line in self.view_card]

    def __str__(self):
        return str('\n'.join([''.join([str(col) for col in lin]) for lin in self.view_card])) + '\n' + 26 * '-'


class LotoGame:
    def __init__(self):
        self.mycard = LotoCard()
        self.my_card = self.mycard.card
        self.compcard = LotoCard()
        self.comp_card = self.compcard.card

    def game(self):
        barrels = random.sample(range(1, 91), 90)
        stop = 0
        full_my_card = 0
        full_comp_card = 0
        while stop == 0:
            next_barrel = barrels.pop()
            print('Новый бочонок: {}. Осталось: {}'.format(next_barrel, len(barrels)))
            print('------ Ваша карточка -----')
            print(self.mycard)
            print('-- Карточка компьютера ---')
            print(self.compcard)
            answ = input('Зачеркнуть цифру? (y/n): ')
            barr_in_card = 0

            for i in range(len(self.my_card)):
                for j in self.my_card[i]:
                    if j == next_barrel:
                        barr_in_card = j
                        break

            if (answ == 'y' and barr_in_card != 0) or (answ == 'n' and barr_in_card == 0):
                print("Верно! \nПродолжаем...")
            else:
                print("Не верно, ты проиграл!")
                break

            for i in range(len(self.my_card)):
                for j in range(len(self.my_card[i])):
                    if self.my_card[i][j] == next_barrel:
                        full_my_card += 1
                        if next_barrel < 10:
                            self.mycard = str(self.mycard).replace(' ' + (str(next_barrel) + ' '), '- ')
                        else:
                            self.mycard = str(self.mycard).replace(str(next_barrel), ' -')
                        self.my_card[i][j] = '-'
                        break

            if full_my_card == 15:
                print('Ты заполнил карту!')
                stop = 1
                break

            for i in range(len(self.comp_card)):
                for j in range(len(self.comp_card[i])):
                    if self.comp_card[i][j] == next_barrel:
                        full_comp_card += 1
                        if next_barrel < 10:
                            self.compcard = str(self.compcard).replace(' ' + (str(next_barrel) + ' '), '- ')
                        else:
                            self.compcard = str(self.compcard).replace(str(next_barrel), ' -')
                        self.comp_card[i][j] = '-'
                        break

            if full_comp_card == 15:
                print('Компьютер заполнил карту!')
                stop = 1
                break


lotogame = LotoGame()
lotogame.game()
