from time import sleep


class TrafficLight:
    def __init__(self):
        self.my_color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in self.my_color:
            print(i)
            if i == 'красный':
                sleep(7)
            elif i == 'желтый':
                sleep(2)
            elif i == 'зеленый':
                sleep(9)


my_traffic = TrafficLight()
my_traffic.running()
