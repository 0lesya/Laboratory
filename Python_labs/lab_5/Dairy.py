from Product import Product


class Dairy(Product):
    def __init__(self, name, size, price, kind):
        Product.__init__(self, name, size, price)
        self.kind = kind

    def __str__(self):
        return Product.__str__(self) + '\tПродукт: {}\n'.format(self.kind)


