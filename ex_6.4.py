class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина {} {} поехала.'.format(self.color, self.name)

    def stop(self):
        return 'Машина {} {} остановилась.'.format(self.color, self.name)

    def turn(self, direction):
        return 'Машина {} {} повернула {}.'.format(self.color, self.name, direction)

    def show_speed(self):
        return 'Машина {} {} едет со скоростью {}.'.format(self.color, self.name, self.speed)


class TownCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Машина {} {} едет со скоростью {}. Превышение скорости!'.format(self.color, self.name, self.speed)
        else:
            return 'Машина {} {} едет со скоростью {}.'.format(self.color, self.name, self.speed)


class SportCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Машина {} {} едет со скоростью {}. Превышение скорости!'.format(self.color, self.name, self.speed)
        else:
            return 'Машина {} {} едет со скоростью {}.'.format(self.color, self.name, self.speed)


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


town = TownCar(70, 'blue', 'Citroen')
print(town.show_speed())
sport = SportCar(200, 'red', 'Ferrari')
print(sport.go(), sport.show_speed(), sport.turn('назад'), sport.stop())
work = WorkCar(35, 'black', 'Ford')
print(work.show_speed())
police = PoliceCar(120, 'white', 'Audi')
print(police.show_speed())
