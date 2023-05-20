from Product import Product
from Dairy import Dairy
from Vegetables import Vegetables
from decimal import *


class WrongSizeValue(Exception):
    def __str__(self):
        return 'Значения не могут быть равны или меньше 0'


class WrongNameValue(Exception):
    def __str__(self):
        return 'Название продукта должно состоять из букв.'


def user_input_product():
    while True:
        try:
            name = input("Название: ")
            if not all(x.isalpha() or x.isspace() for x in name):
                raise WrongNameValue
            product_size = tuple(map(int, input("Размер: ").split()))
            if (len(product_size)) != 3:
                print("Размер состоит из трех числовых значений.")
                continue
            if (product_size[0] and product_size[1] and product_size[2]) <= 0:
                raise WrongSizeValue
            price = Decimal(input("Цена: "))
            if price <= 0:
                raise WrongSizeValue
            product = Product(name, product_size, price)
            break
        except Exception as e:
            print("Введены некорректные данные: " + str(e))
    return product


def user_input_dairy():
    while True:
        try:
            name = input("Название: ")
            if not all(x.isalpha() or x.isspace() for x in name):
                raise WrongNameValue
            product_size = tuple(map(int, input("Размер: ").split()))
            if (len(product_size)) != 3:
                print("Размер состоит из трех числовых значений.")
                continue
            if (product_size[0] and product_size[1] and product_size[2]) <= 0:
                raise WrongSizeValue
            price = Decimal(input("Цена: "))
            if price <= 0:
                raise WrongSizeValue
            kind = input("Тип: ")
            product = Dairy(name, product_size, price, kind)
            break
        except ValueError as e:
            print("Введены некорректные данные: " + str(e))
    return product


def user_input_vegetables():
    while True:
        try:
            name = input("Название: ")
            if not all(x.isalpha() or x.isspace() for x in name):
                raise WrongNameValue
            product_size = Decimal(input("Введите размер, если он есть: "))
            if product_size < 0:
                print("Значения размера не могут быть меньше 0")
                continue
            price = Decimal(input("Цена: "))
            if price <= 0:
                raise WrongSizeValue
            weight = Decimal(input("Введите вес: "))
            if weight <= 0:
                raise WrongSizeValue
            product = Vegetables(name, product_size, price, weight)
            break
        except Exception as e:
            print("Введены некорректные данные: " + str(e))
    return product


def menu():
    try:
        answer = int(input("Выберите тип продукта: \n1. Продукт\n2. Молочная продукция\n3. Овощи\n"))
        if answer == 1:
            print("Введите данные для класса 'Продукт': ")
            return user_input_product()
        elif answer == 2:
            print("Введите данные для класса 'Молочная продукция': ")
            return user_input_dairy()
        elif answer == 3:
            print("Введите данные для класса 'Овощи': ")
            return user_input_vegetables()
        else:
            print("Такого выбора нет.")
    except ValueError as e:
        print("Некорректный ответ: "+str(e))
        return menu()
