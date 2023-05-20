import os
from shannon.func import amount_lines
from shannon.Encoder import *
from rle.RLE_flag import *
from LZ.lz_encoder import *
archive = open('archive.NIYSOI', 'w', encoding='utf-8')


def str2hex(s):
    return bytes(s.encode('utf-8')).hex()


signature = str(str2hex('NIYSOI'))
version = str2hex('0003')
algorithms = []


def get_text_from_file(file):
    texts = ""
    for line in file.readlines():
        texts += line
    return texts


filename_s = []
lens = []
for filename in os.listdir('Files'):
    len_file = amount_lines('Files/'+filename)
    lens.append(str(len_file))
    lens.append(' ')
    #filename = str2hex(filename)
    filename_s.append(str(filename))
    filename_s.append(' ')

length = str2hex(str(os.stat('archive.NIYSOI').st_size + sum(list(map(int, (''.join(lens)).split())))))
archive.writelines([signature+'\n', version+'\n', length+'\n', *filename_s, '\n', *lens, '\n'])
dict_list = []

for item_file in os.listdir('Files'):
    with open('Files/'+item_file, 'rb') as f:
        binary_code = (' '.join(format(i, 'b') for i in f.read()))

    print("len of binary code: ", len(binary_code))
    file = open('Files/'+item_file, 'r', encoding='utf-8')
    text = get_text_from_file(file)
    coder = Encoder()
    cipher = coder.encrypt(text)
    file.close()
    print("len of cipher: ", len(cipher))
    another_file = open('Files/' + item_file, 'r', encoding='utf-8')
    text = get_text_from_file(another_file)
    rle_algorithm = encode(bytes(text.encode('utf-8')).hex())
    print("len of RLE: ", get_len_code(rle_algorithm))
    another_file.close()
    file_lz = open('Files/' + item_file, 'r', encoding='utf-8')
    text = get_text_from_file(file_lz)
    lz_algorithm = lz_encoder(text)
    print("len of LZ: ", len(lz_algorithm), "\n")
    file_lz.close()

    if len(binary_code) < len(cipher):
        archive.write(text)
        archive.write('\n')
        algorithms.append('00 00 00 00 00 00')
    elif len(cipher) < get_len_code(rle_algorithm):
        archive.write(cipher)
        archive.write('\n')
        dict_list.append(coder.encode_dict)
        algorithms.append('00 00 00 00 00 01')
    elif get_len_code(rle_algorithm) < len(lz_algorithm):
        archive.write(rle_algorithm)
        archive.write('\n')
        algorithms.append('00 00 00 00 00 02')
    else:
        archive.write(lz_algorithm)
        archive.write('\n')
        algorithms.append('00 00 00 00 00 03')

for algorithm in algorithms:
    archive.write(algorithm)
    archive.write('\n')

archive.close()
