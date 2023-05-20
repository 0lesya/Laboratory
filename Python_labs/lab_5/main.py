from Input_functions import *


stuff = menu()
print(stuff)
stuff.discount(input("Введите значение скидки: "))
print('Цена со скидкой: '+stuff.price.__str__())
stuff.size = tuple(input("Введите новый размер продукта: ").split())
print(stuff.size)
stuff.size = tuple(input("Введите новый размер продукта: ").split())
print('Размер товара изменен на: '+stuff.size.__str__())
print()

milk = menu()
print(milk)
print('Введите размер коробки: ')
box_size = tuple(input().split())
print('Количество пакетов молока в коробке для перевоза: '+str(milk.box_size(box_size)))

potato = menu()
print(potato)
potato.weight = input("Введите новый вес: ") #проверка неправильного ввода веса
print(potato)
potato.discount(24)
print('Цена за '+str(potato.weight)+' кг со скидкой: '+str(potato.price))

print("\n\tСохранение в файл")
file = open("file.txt", "wb+")
try:
    file.write(potato.__str__().encode())
    file.write(milk.__str__().encode())
    file.write(stuff.__str__().encode())
except Exception as e:
    print('Ошибка записи в файл: '+str(e))
finally:
    file.close()
    print("Завершение работы с файлом")
print("\n\tЧтение из файла")
file = open("file.txt", "rb+")
try:
    for line in file:
        print(line.decode())
except Exception as e:
    print('Ошибка чтения из файла: '+str(e))
finally:
    file.close()
    print("Завершение работы с файлом")

