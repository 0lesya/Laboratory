#  lab 4
from math import *


#  расчет длины файла в символах первичного алфавита - байтах.
def len_calculation(file):
    length = 0
    for line in file:
        length += len(bytes(line, 'utf-8').hex())
    file.close()
    return length


#  количество вхождений подстрок
def v_calculation(file):
    count_dict = dict()
    for line in file:
        line = bytes(line, 'utf-8').hex()
        for i in range(len(line)-1):
            okt = line[i]+line[i+1]
            if okt not in count_dict.keys():
                count_dict[okt] = line.count(okt)
            elif okt in count_dict.keys():
                count_dict[okt] += line.count(okt)
    for i in range(len(count_dict)):
        print('Подстрока ' + str(list(count_dict.keys())[i]) + ' встречается ' + str(round(
           count_dict[list(count_dict.keys())[i]], 7))+' раз')
    print('')
    file.close()
    return count_dict


#  общее количество вхождений любых двух символьных подстрок
def calculation_two_substrings(file):
    count_dict = dict()
    for line in file:
        line = bytes(line, 'utf-8').hex()
        for i in range(len(line) - 1):
            okt = line[i] + line[i + 1]
            if okt[0] not in count_dict.keys():
                count_dict[okt[0]] = line.count(okt[0])
            elif okt[0] in count_dict.keys():
                count_dict[okt[0]] += line.count(okt[0])
    for i in range(len(count_dict)):
        print("Подстрока, начинающаяся с " + "'", str(list(count_dict.keys())[i]), "'" + ' встречается ' + str(round(
            count_dict[list(count_dict.keys())[i]], 7)) + ' раз')
    print('')
    file.close()
    return count_dict


#  безусловная вероятность для каждого символа
def unconditional_probability(file):
    sum_alf = 0
    count_dict = dict()
    for line in file:
        line = bytes(line, 'utf-8').hex()
        for i in line:
            if i not in count_dict.keys():
                count_dict[i] = line.count(i)
            else:
                count_dict[i] += line.count(i)
            sum_alf += line.count(i)
    for key in count_dict.keys():
        value = count_dict[key] / sum_alf
        count_dict[key] = value
    count_dict = dict(sorted(count_dict.items()))
    for i in range(len(count_dict)):
        print('Безусловная вероятность символа ' + str(list(count_dict.keys())[i]) + ' равна ' + str(round(
            count_dict[list(count_dict.keys())[i]], 5)))
    print('')
    return count_dict


# вероятности подстрок
def substring_probability(sub_dict):
    sums = 0
    prob_dict = dict()
    for value in sub_dict.values():
        sums += value
    for key, value in sub_dict.items():
        prob_dict[key] = value / sums
    return prob_dict


#  условная вероятность
def conditional_probability(sub_dict, symbol_dict):
    cond_prob = dict()
    for key in sub_dict.keys():
        for skey in symbol_dict.keys():
            if skey in key:
                cond_prob[key] = sub_dict[key] / symbol_dict[skey]
    for i in range(len(cond_prob)):
        print('Условная вероятность пары символов ' + str(list(cond_prob.keys())[i]) + ' равна ' + str(round(
            cond_prob[list(cond_prob.keys())[i]], 5)))
    print('')


#  суммарное количество информации
def information(symbol_dict):
    sum_inf_bite = 0
    sum_inf_byte = 0
    for value in symbol_dict.values():
        sum_inf_bite += value * log2(1/value)
        sum_inf_byte += value * log(1/value, 256)
    print('Количество информации в битах: ', sum_inf_bite)
    print('Количество информации в байтах: ', sum_inf_byte)


def open_file(filename):
    file = open(filename, 'r')
    return file


fileName = 'C:/Users/Олеся/3 course/OTIK_labs/otik/labs-files/files' \
           '/plaintext/Rewards and Fairies, by Rudyard Kipling.txt'

print('Длина файла в символах первичного алфавита: ', len_calculation(open_file(fileName)), '\n')

calculation_two_substrings(open_file(fileName))

conditional_probability(substring_probability(v_calculation(open_file(fileName))),
                        unconditional_probability(open_file(fileName)))

information(unconditional_probability(fileName))
