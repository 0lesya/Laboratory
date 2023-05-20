#mport multiprocessing
k = int(input())


def func(num):
    i = 10
    while num:
        i += 9
        if sum(map(int, str(i))) == 10:
            num -= 1
    print(i)


func(k)
