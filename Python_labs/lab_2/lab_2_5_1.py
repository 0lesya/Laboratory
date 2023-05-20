import os


def input_list():
    try:
        l, r = int(input()), int(input())
        if l < 0 or r < 0 or r > 100 or l > 100 or l > r:
            print(
                'Числа должны находить в диапазоне от 0 до 100, и число слева меньше того, что справа.\nПопробуйте еще раз')
            return input_list()
        else:
            return 1024 * l, 1024 * r
    except Exception:
        print("Введено не число. Попробуйте еще раз.")
        return input_list()


left, right = input_list()
count = 0
for file in os.listdir('example'):
    if right >= int(os.path.getsize('example/' + file)) >= left:
        count += 1
    else:
        continue

print("Количество файлов, размер которых находится между " + str(int(left / 1024)) + ' Кб и ' + str(
    int(right / 1024.0)) + ' Кб: ' + str(count))
