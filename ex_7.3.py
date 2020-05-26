class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return 'Результат операции {}'.format(self.quantity * "*")

    def __add__(self, other):
        return 'Сложение {}'.format(Cell(self.quantity + other.quantity))

    def __sub__(self, other):
        return 'Вычитание {}'.format(Cell(self.quantity - other.quantity))

    def __mul__(self, other):
        return 'Умножение {}'.format(Cell(int(self.quantity * other.quantity)))

    def __truediv__(self, other):
        return 'Деление {}'.format(Cell(round(self.quantity // other.quantity)))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cell = Cell(12)
new_cell = Cell(2)
print(cell)
print(cell + new_cell)
print(cell - new_cell)
print(cell * new_cell)
print(cell / new_cell)
print(cell.make_order(5))
print(new_cell.make_order(2))
