import math
from decimal import *


class Product:
    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, names):
        if all(x.isalpha() or x.isspace() for x in names):
            self.__name = names
        else:
            return 'Название продукта должно состоять из букв.'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, tuple) and len(size) == 3:
            try:
                size = tuple(map(int, size))
                if (size[0] and size[1] and size[2]) <= 0:
                    print('Значения размера продукта должны быть >0')
                else:
                    self.__size = size
            except ValueError as e:
                print("Значение размера должны быть числовыми: "+str(e))
        else:
            print('Неверный ввод данных размера')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        str_error = 'Недопустимая цена'
        if isinstance(price, float) or isinstance(price, int):
            if 0.01 <= price:
                self.__price = price
            else:
                print(str_error)
        else:
            print(str_error)

    def discount(self, dis):
        try:
            dis = Decimal(dis)
            self.__price = round(self.__price*(1-dis/100), 2)
        except Exception as e:
            print("Неверное значение скидки: "+str(e))

    def box_size(self, sizes):
        if isinstance(sizes, tuple) and len(sizes) == 3:
            try:
                sizes = tuple(map(int, sizes))
                count = 0
                value = sizes[0]*sizes[1]*sizes[2]
                size = [self.__size[0], self.__size[1], self.__size[2]]
                result_size = math.prod(size)
                if sizes[0] and sizes[1] and sizes[2] > min(size):
                    while value >= result_size:
                        value -= result_size
                        count += 1
                    return count
                else:
                    return 'Размер коробки ' + str(sizes)+' не подходит'
            except ValueError as e:
                return "Значение размера должны быть числовыми: "+str(e)
        else:
            print("Размер состоит из трех числовых значений")

    def __add__(self, other):
        full_price = self.price + other.price
        return full_price

    def __str__(self):
        return 'Название продукта: "{}"\tРазмер: {}\tЦена: {}'.format(self.__name, self.__size, self.__price)


