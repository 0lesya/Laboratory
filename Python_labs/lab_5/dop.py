def strange(m):
    count = 0
    while len(set(m)) > 1:
        m[m.index(max(m))] = max(m)-min(m)
        count += 1
    return count


with open('input.txt', 'r') as file:
    list_num = [int(i) for i in file.readline().split()]
    with open('output.txt', 'w') as file_out:
        file_out.write(str(strange(list_num)))


