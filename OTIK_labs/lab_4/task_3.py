#  RLE с флаг-битами (цепочки несжатых символов и сжатые цепочки)


def main():
    our_message = 'FFF000000123456789ABCDEFFFF0FFF00000000000000000112233445566778899AABBCCDDEEFFF0'
    encoded_message = encode(our_message)
    decoded_message = decode(encoded_message)

    print("Исходное сообщение: ", our_message)
    print("Закодированное сообщение: ", encoded_message)
    print("Декодированное сообщение: ", decoded_message)
    print(our_message == decoded_message)

    print('Исходная длина сообщения: ', len(our_message))
    print('Длина закодированного сообщения: ', get_len_code(encoded_message))


def encode(sequence):
    encoded_message = ""
    one_count = 0
    i = 0
    chars_list = ''

    while i <= (len(sequence) - 1):
        count = 1
        ch = sequence[i]
        j = i
        while j < (len(sequence) - 1):
            if sequence[j] == sequence[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        if ch == '0' and (count == 1 or count == 2):
            encoded_message = encoded_message + str(0)+str(count)+ch
            i = j + 1
            continue

        if count == 1 or count == 2:
            one_count += count
            chars_list += ch*count
            i = j + 1
            continue
        elif count != 1 and one_count != 0:
            encoded_message = check_one_value(encoded_message, one_count, chars_list)
            encoded_message = check_more_than(encoded_message, count, ch)
            one_count = 0
            chars_list = ''
        else:
            encoded_message = check_more_than(encoded_message, count, ch)
        i = j + 1
    return encoded_message


def check_one_value(message, counts, chars):
    if counts > 7:
        while counts > 7:
            pr = 7
            message = message + str(0)+str(pr) + chars[:7]
            counts = counts - pr
            chars = chars[7:]
            if counts > 7:
                continue
            message = message + str(0) + str(counts) + chars
        return message
    else:
        return message + str(0) + str(counts) + chars


def check_more_than(message, counts, cha):
    if counts > 7:
        while counts > 7:
            pr = 7
            message = message + str(1)+str(pr) + cha
            counts = counts - pr
            if counts > 7:
                continue
            if counts != 1:
                message = message + str(1)+str(counts) + cha
            else:
                message = message + str(0) + str(counts) + cha
        return message
    else:
        message = message + str(1) + str(counts) + cha
        return message


def decode(sequence):
    decoded_message = ""
    i = 0
    while i <= (len(sequence) - 1):
        ch = sequence[i]
        if ch == '1':
            decoded_message = decoded_message + int(sequence[i + 1]) * sequence[i+2]
            i += 3
        else:
            for j in range(i+2, (i+2)+int(sequence[i+1])):
                decoded_message = decoded_message + sequence[j]
            i += 2+int(sequence[i+1])
    return decoded_message


def get_len_code(sequence):
    length = 0
    i = 0
    while i <= (len(sequence) - 1):
        ch = sequence[i]
        if ch == '1':
            length += 2
            i += 3
        else:
            length += 1+int(sequence[i + 1])
            i += 2 + int(sequence[i + 1])
    return length


if __name__ == '__main__':
    main()
