from operator import itemgetter

encode_list = []
encode_dict = {}


def encrypt(information):
    shannon_fano(information)
    return write_encrypt(information)


def shannon_fano(information):
    probabilities_dict = create_probabilities_dict(information)
    symbols = list(probabilities_dict.keys())
    weights = list(probabilities_dict.values())
    encode(weights, "")
    create_encode_dictionary(symbols)


def create_probabilities_dict(str):
    d = {}
    for s in str:
        if d.__contains__(s) == False:
            d[s] = 1
        else:
            d[s] += 1
    return dict(sorted(d.items(), reverse=True, key=itemgetter(1)))


def encode(weights, str):
    if len(weights) == 1:
        encode_list.append(str)
        return
    middle = count_separation_index(weights)
    encode(create_subset(weights, 0, middle), str + "1")
    encode(create_subset(weights, middle, len(weights)), str + "0")


def count_separation_index(weights):
    l = 0
    r = len(weights)
    m = int((l + r) / 2)
    while True:
        left_sum = count_sum(create_subset(weights, l, m))
        right_sum = count_sum(create_subset(weights, m, len(weights)))
        if left_sum <= right_sum:
            return m
        else:
            r = m
            m -= 1


def create_subset(set, start_index, last_index):
    subset = []
    for i in range(start_index, len(set)):
        if i == last_index:
            break
        subset.append(set[i])
    return subset


def count_sum(list):
    sum_elements = 0
    for element in list:
        sum_elements += element
    return sum_elements


def create_encode_dictionary(symbols):
    for i in range(len(symbols)):
        encode_dict[symbols[i]] = encode_list[i]
    return encode_dict


def write_encrypt(information):
    chifer = ""
    for byte in information:
        chifer += encode_dict[byte]
    return chifer


print(encrypt("небо нло зелено"))