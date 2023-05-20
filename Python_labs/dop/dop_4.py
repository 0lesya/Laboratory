def strange():
    with open('input.txt', 'r') as file, open('output.txt', 'w') as file_out:
        list_num = [int(i) for i in file.readline().split()]
        count = 0
        while len(set(list_num)) > 1:
            list_num[list_num.index(max(list_num))] = max(list_num) - min(list_num)
            count += 1
        file_out.write(str(count))


strange()
