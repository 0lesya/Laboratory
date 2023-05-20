import os
import binascii
from func import amount_lines
from Encoder import *

archive = open('archive.NIYSOI', 'w', encoding='utf-8')

signature = '4e49 5953 4f49'
version = '0002'
algorithms = '00 00 00 00 00 01'


def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))


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
archive.writelines([signature+'\n', version+'\n', algorithms+'\n', length+'\n', *filename_s, '\n', *lens, '\n'])
dict_list = [[], [], []]
kostyl=0
for file in os.listdir('Files'):
    file = open('Files/'+file, 'r', encoding='utf-8')
    lines = file.readlines()

    for i in range(len(lines)):

        coder = Encoder()
        archive.write(coder.encrypt(lines[i]))
        archive.write('\n')
        dict_list[kostyl].append(coder.encode_dict)
    kostyl+=1
    file.close()
    archive.write('\n')

archive.close()
