import unittest
from Product import Product


class ProductTest(unittest.TestCase):

    def test_str_product(self):
        test_var = Product('name', (100, 100, 100), 100)
        self.assertEqual(test_var.__str__(), 'Название продукта: "name"\tРазмер: (100, 100, 100)\tЦена: 100')


if __name__ == "__main__":
    unittest.main()
