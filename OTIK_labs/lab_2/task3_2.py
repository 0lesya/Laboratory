import chardet
from functions import count_oktets
directory = 'C:/Users/Олеся/3 course/OTIK_labs/otik/labs-files/variants/L2'
filename = directory + '/2.txt'
dict_chardet = chardet.detect(open(filename, 'rb').read())
file = open(filename, 'r', encoding=dict_chardet['encoding'])
count_oktets(file)
file.close()
print(dict_chardet)

