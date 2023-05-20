from Product import Product
from Dairy import Dairy
from Vegetables import Vegetables

stuff = Product('Полка', (100, 150, 10), 1049)
print(stuff)
stuff.discount(17)
print('Цена со скидкой: '+stuff.price.__str__())
stuff.size = 0.001 #протестируем неправильный ввод данных размера
print(stuff.size)
stuff.size = (150, 100, 15)
print('Размер товара изменен на: '+stuff.size.__str__())
print()

milk = Dairy('Домик в деревне', (12, 24, 12), 65, 'Молоко')
print(milk)
print('Количество пакетов молока в коробке для перевоза: '+str(milk.box_size((144, 48, 24))))
print(milk.box_size((144, 48, 11))) #коробка хотя бы по одному параметру меньше размера товара
print()

potato = Vegetables('Картошка', 0, 25, 0.3)
print(potato)
potato.weight = -5 #проверка неправильного ввода веса
potato.weight = 1.5
print(potato)
potato.discount(24)
print('Цена за '+str(potato.weight)+' кг со скидкой: '+str(potato.price))

print('Использование перегруженного оператора сложения: '+str(milk+stuff))


