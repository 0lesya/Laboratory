try:
    num = [int(i) for i in input().split()]
    k = 0
except Exception:
    print('Введен не список чисел, попробуйте еще раз')
    num = [int(i) for i in input().split()]
    k = 0
print(num)
print(" ")


def to_zero(nums, it):
    d = it
    for i in range(len(nums)):
        while nums[i] != 0:
            nums[i] -= 1
            d += 1
            print(nums)
            print('')
    return d


while 0 not in num:
    for i in range(len(num)):
        if num[i] != 0:
            num[i] -= 1
        else:
            continue
    print(num)
    k += 1
    print('')

if 1 in num:
    num.remove(1)
k = to_zero(num, k)
print(k)
