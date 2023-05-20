from Product import Product


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
        if isinstance(weight, float) or isinstance(weight, int):
            if weight > 0:
                self.__weight = weight
            else:
                print('Вес не может быть отрицательным')
        else:
            print('Ошибка ввода веса продукта')

    @property
    def price(self):
        return self.__price*self.__weight

    @price.setter
    def price(self, price):
        str_error = 'Недопустимая цена'
        if isinstance(price, float) or isinstance(price, int):
            self.__price = price*self.__weight
        else:
            print(str_error)

    def discount(self, dis):
        self.__price = round(self.__price*self.__weight*(1-dis/100), 2)

    def __str__(self):
        return 'Название продукта: "{}"\tЦена: {}\tВес: {}'.format(self.name, self.price, self.weight)
