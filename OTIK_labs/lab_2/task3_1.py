import chardet
import os
from functions import count_oktets
files = 'C:/Users/Олеся/3 course/OTIK_labs/otik/labs-files/files/plaintext/Кодировки разные'
for filename in os.listdir(files):
    dict_chardet = chardet.detect(open(files + '/' + filename, 'rb').read())
    #print(dict_chardet)
    test_file = open(files + '/' + filename, 'r', encoding=dict_chardet['encoding'])
    print(filename)
    count_oktets(test_file)
    test_file.close()

