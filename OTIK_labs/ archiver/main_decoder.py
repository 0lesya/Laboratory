import enum
import os
from shannon.Encoder import *
from main_encoder import dict_list
from rle.RLE_flag import *
from LZ.decodeLZ import *


def get_algorithms_line():
    step = len(filenames)
    return [i.replace('\n', '') for i in reading_archive[16:]]


def get_encrypted_files_as_lines():
    return reading_archive[encrypt_info_in_zag_line:encrypt_info_in_zag_line + 11]


def get_file_name_from_files(index):
    f_name = filenames[index][2:len(filenames[index]) - 1]
    return f_name


def get_decode_file(i):
    if '2' in ''.join(algorithms[i]):
        return bytes.fromhex(decode(encrypted_file_in_zag[i])).decode('utf-8')
    #elif '1' in ''.join(algorithms[i]):
     #   decode_dictionary = dict_list[i]
      #  return decoder.decode(encrypted_file_in_zag[i], decode_dictionary)
    elif '3' in ''.join(algorithms[i]):
        return lz_decoder(encrypted_file_in_zag[i])
    else:
        return bytes.fromhex(encrypted_file_in_zag[i])


class Archive(enum.Enum):
    Signature = 0
    File_names = 3
    Lengths = 4

archive = open('archive.NIYSOI', 'r', encoding='utf-8')
my_signature = "".join([hex(ord(i))[2:] for i in os.path.splitext('archive.NIYSOI')[-1]][1:])
reading_archive = archive.readlines()  # сохраняем в список строки по очереди
signature = reading_archive[Archive.Signature.value]
filenames = reading_archive[Archive.File_names.value].split()
lens = list(map(int, reading_archive[Archive.Lengths.value].split()))
decoder = Decoder()
encrypt_info_in_zag_line = 5
if str(my_signature) in str(signature):
    algorithms = get_algorithms_line()
    encrypted_file_in_zag = get_encrypted_files_as_lines()
    j = 0
    for _ in range(4):
        print(lens[_])
        file_name = filenames[_]
        print(file_name)
        for i in range(lens[j]):
            new_file = open(file_name, mode='w+', encoding='utf-8')
            new_file.write(str(get_decode_file(i)))
            new_file.close()
        j+=1

archive.close()
