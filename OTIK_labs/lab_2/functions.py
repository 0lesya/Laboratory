def count_oktets(file):
    count_dict = dict()
    count_not_print = dict()
    sum_alf = 0
    lines = file.read()
    for line in lines:
        for i in line:
            if i.isprintable() and i not in count_dict.keys():
                count_dict[i] = line.count(i)
                sum_alf += line.count(i)
            elif i.isprintable() and i in count_dict.keys():
                count_dict[i] += line.count(i)
                sum_alf += line.count(i)
            elif i not in count_dict.keys():
                count_not_print[i] = line.count(i)
                sum_alf += line.count(i)
            else:
                count_not_print[i] += line.count(i)
                sum_alf += line.count(i)
            line.replace(i, '')

    for key in count_dict.keys():
        value = count_dict[key] / sum_alf
        count_dict[key] = value
    for key in count_not_print.keys():
        value = count_not_print[key] / sum_alf
        count_not_print[key] = value
    sorted_values = sorted(count_dict.values(), reverse=True)
    sorted_not_print = sorted(count_not_print.values(), reverse=True)

    new_sorted_dictionary = {}
    new_sorted_not_print = {}

    for i in sorted_values:
        for k in count_dict.keys():
            if count_dict[k] == i:
                new_sorted_dictionary[k] = count_dict[k]
                break
    for i in sorted_not_print:
        for k in count_not_print.keys():
            if count_not_print[k] == i:
                new_sorted_not_print[k] = count_not_print[k]
                break

    print('Весь размер: ', sum_alf)

    print('4 наиболее частых октетов')
    for i in range(4):
        print('символ ' + str(list(new_sorted_dictionary.keys())[i]) + ' с частотой ' + str(round(
            new_sorted_dictionary[list(new_sorted_dictionary.keys())[i]], 5)))
    print('')

    print('Наиболее частые непечатаемые октеты:')
    for key in new_sorted_not_print.keys():
        print('символ '+str(key)+'с частотой '+str(round(new_sorted_not_print[key], 6)) + '\n')
