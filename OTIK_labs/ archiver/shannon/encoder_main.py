import os
import binascii
from func import amount_lines
from Encoder import *

archive = open('archive.NIYSOI', 'w', encoding='utf-8')

signature = '4e49 5953 4f49'
version = '0002'
algorithms = []


def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))


def get_text_from_file(file):
    text = ""
    for line in file.readlines():
        text += line
    return text


filename_s = []
lens = []
for filename in os.listdir('Files'):
    len_file = amount_lines('Files/'+filename)
    lens.append(str(len_file))
    lens.append(' ')
    filename = str2hex(filename)
    filename_s.append(str(filename))
    filename_s.append(' ')

length = str(os.stat('archive.NIYSOI').st_size + sum(list(map(int, (''.join(lens)).split()))))
archive.writelines([signature+'\n', version+'\n', length+'\n', *filename_s, '\n', *lens, '\n'])
dict_list = []

for file in os.listdir('Files'):
    with open('Files/'+file, 'rb') as f:
        binary_code = (' '.join(format(i, 'b') for i in f.read()))

    print("len of binary code: ", len(binary_code))
    file = open('Files/'+file, 'r', encoding='utf-8')
    text = get_text_from_file(file)
    coder = Encoder()
    cipher = coder.encrypt(text)
    print("len of cipher: ", len(cipher), "\n")
    if( len(binary_code) < len(cipher) ):
        archive.write(text)
        archive.write('\n')
        algorithms.append('00 00 00 00 00 00')
    else:
        archive.write(cipher)
        archive.write('\n')
        dict_list.append(coder.encode_dict)
        algorithms.append('00 00 00 00 00 01')
    file.close()

for algorithm in algorithms:
    archive.write(algorithm)
    archive.write('\n')





archive.close()
