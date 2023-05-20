import enum
import os
from Encoder import *
from encoder_main import dict_list


def get_algorithms_line():
    return [int(i) for i in zag[2][:(len(zag[2]) - 1)].replace(' ', '')]


def get_encrypted_files_as_lines():
    return zag[encrypt_info_in_zag_line:encrypt_info_in_zag_line + len(filenames)]


def get_file_name_from_files(index):
    f_name = filenames[index][2:len(filenames[index]) - 1]
    return bytes.fromhex(f_name).decode('utf-8')


def get_decode_file(i):
    if sum(algorithms) == 0:
        return bytes.fromhex(encrypted_file_in_zag[i])
    else:
        return decoder.decode(encrypted_file_in_zag[i], decode_dictionary)


class Archive(enum.Enum):
    Signature = 0
    File_names = 4
    Lengths = 5


archive_name = 'archive.NIYSOI'
archive = open('archive.NIYSOI', 'r', encoding='utf-8')
my_signature = "".join([hex(ord(i))[2:] for i in os.path.splitext('archive.NIYSOI')[-1]][1:])
zag = archive.readlines()  # сохраняем в список строки по очереди
signature = zag[Archive.Signature.value][:(len(zag[0]) - 1)].replace(' ',
                                                                     '')
filenames = zag[Archive.File_names.value].split()
lens = zag[Archive.Lengths.value].split()
decoder = Decoder()
encrypt_info_in_zag_line = 6
if my_signature == signature:
    algorithms = get_algorithms_line()
    encrypted_file_in_zag = get_encrypted_files_as_lines()
    for i in range(len(encrypted_file_in_zag)):
        decode_dictionary = dict_list[i]
        file_name = get_file_name_from_files(i)
        new_file = open(file_name, mode='w+', encoding='utf-8')
        new_file.write(get_decode_file(i))
        new_file.close()
archive.close()
