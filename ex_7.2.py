class Clothes:
    def __init__(self, v, h):
        self.coat = v
        self.suit = h

    @property
    def sq_coat(self):
        return self.coat/6.5 + 0.5

    @property
    def sq_suit(self):
        return 2*self.suit + 0.3

    @property
    def sq_full(self):
        return self.sq_coat + self.sq_suit

    def __str__(self):
        return 'Общая площадь ткани {}'.format(self.sq_full)


class Coat(Clothes):
    def __init__(self, v):
        self.coat = v

    def __str__(self):
        return 'Площадь ткани на пальто {}'.format(self.sq_coat)


class Suit(Clothes):
    def __init__(self, h):
        self.suit = h

    def __str__(self):
        return 'Площадь ткани на костюм {}'.format(self.sq_suit)


size = 650
height = 100
print('{}\n{}'.format(Coat(size), Suit(height)))
clothes = Clothes(size, height)
print(clothes)
