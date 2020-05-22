class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('"Запуск отрисовки {}."'.format(self.title))


class Pen(Stationery):
    def draw(self):
        print('"Отрисовка ручкой {}."'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('"Отрисовка карандашом {}."'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('"Отрисовка маркером {}."'.format(self.title))


stationery = Stationery('номер_1')
stationery.draw()
pen = Pen('номер_2')
pen.draw()
pencil = Pencil('номер_3')
pencil.draw()
handle = Handle('номер_4')
handle.draw()
