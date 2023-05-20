try:
    n = int(input())
except Exception:
    print('Введен не список чисел, попробуйте еще раз')

data = dict()
count_dict = dict()
count_v = []

for _ in range(n):
    key = tuple(int(i) for i in input().split())
    if key in count_dict.keys():
        count_dict[key].append(int(input()))
    else:
        count_v.append(int(input()))
        count_dict[key] = count_v
        count_v = []
for key in count_dict.keys():
    value = len(set(count_dict[key]))
    count_dict[key] = value

print(count_dict)
