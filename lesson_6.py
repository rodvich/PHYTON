# def print_human_name(human):
#     print(human['name'])
#
# h1 = {'name': 'Pavel'}
# h2 = {'name': 'Alex'}
#
# print_human_name(h1)
# print_human_name(h2)
#
# h3 = {'full_name': 'Mihail'}
# print_human_name(h3)

class Phone:    # CamelStyle
    def __init__(self, phone_model):    # происходит всегда вначале
        self.model = phone_model
        self._id = 123123
        self._loading()
        self.__bla = 'bla'  # Приватная функция

    def call(self):
        print('Calling...')

    def _loading(self):     # Скрытая (защищенная) функция
        print(self.model, '...loading...')

    def get_id(self):
        return self._id


# my_phone_1 = Phone('nokia1100')
# # my_phone_1.loading()
# # print(my_phone_1.model)
# my_phone_1.call()
#
# # my_phone_1._loading()
# # print(my_phone_1.get_id())
# # print(my_phone_1._Phone__bla)   # name._ClassName_foo
# # my_phone_2 = Phone()
# # my_phone_1.call()
# # my_phone_2.call()

class SmartPhone(Phone):     # Родитель Phone

    def sms(self):
        print('sms')

    def email(self):
        print('email')


# mys = SmartPhone('nokia 6600')
# mys.call()
# mys.sms()

class IPhone(SmartPhone):

    def __init__(self, phone_model):
        super().__init__(phone_model)
        print('show logo')

    def player(self):
        print('music')

    def browser(self):
        print('browser opening...')

    def sms(self):
        print('Imessege sending...')


# iphone = IPhone('6')
# iphone.sms()

class NextPhone(IPhone):
    def pay(self):
        print('pay')


class Huawei(NextPhone):
    pass


class Samsung(NextPhone):
    pass



class Player:
    def player(self):
        print('music playing')


class Navigator:
    def nav_method(self):
        print('navigator')


class MPhone(Player, Navigator):    # Кто первый - тот и папа
    def mphone_method(self):
        print('mphone_method')


# mp = MPhone()
# mp.player()
# mp.nav_method()
# mp.mphone_method()

class Auto:
    def auto_start(self, param1, param2=None):
        if param2 is not None:
            print(param1 + param2)
        else:
            print(param1)


# a = Auto()
# a.auto_start(10)
# a.auto_start(10, 50)
