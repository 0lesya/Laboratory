from Product import Product
from decimal import *

class Vegetables(Product):
    def __init__(self, name, size, price, weight):
        Product.__init__(self, name, size, price)
        self.__weight = weight
        self.__price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        try:
            weight=Decimal(weight)
            if weight > 0:
                self.__weight = weight
            else:
                print('Вес не может быть отрицательным')
        except ValueError as err:
            print('Ошибка ввода веса продукта: '+ str(err))

    @property
    def price(self):
        try:
            return Decimal(self.__price) * Decimal(self.__weight)
        except Exception as exc:
            print(exc)

    @price.setter
    def price(self, price, weight):
        try:
            price=Decimal(price)
            weight = Decimal(weight)
            self.__price = price*weight
        except ValueError as err:
            print("Неверные значения: "+str(err))

    def discount(self, dis):
        try:
            dis = Decimal(dis)
            self.__price=Decimal('{:.2}'.format(self.__price * self.__weight * (1 - dis / 100)))
        except Exception as e:
            print('Неверное значение скидки.')

    def __str__(self):
        return 'Название продукта: "{}"\tЦена: {}\tВес: {}\n'.format(self.name, self.price, self.weight)
