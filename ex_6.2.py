class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return self._width * self._length * 25 * 5 / 1000


road = Road(20, 5000)
print('{:.0f} т'.format(road.weight()))
