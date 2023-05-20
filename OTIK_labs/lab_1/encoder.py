import os
import binascii
from func import amount_lines

archive = open('archive.NIYSOI', 'w', encoding='utf-8')

signature = '4e49 5953 4f49'
version = '0001'
algorithms = '00 00 00 00 00 00'


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

for file in os.listdir('Files'):
    filename = file
    file = open('Files/'+file, 'r', encoding='utf-8')
    for line in file.readlines():
        archive.write(line.encode("utf-8").hex())
        archive.write('\n')
    file.close()
    archive.write('\n')
archive.close()
