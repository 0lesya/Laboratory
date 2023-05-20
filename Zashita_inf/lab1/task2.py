import chardet
file = 'file2.txt'
dict_chardet = chardet.detect(open(file, 'rb').read())
print(dict_chardet)
test_file = open(file, 'r', encoding=dict_chardet['encoding'])
lines = test_file.readlines()

count_dict = dict()

for line in lines:
    line = str(line.encode()).split('\\')[1:-1]
    for byte in line:
        if byte not in count_dict.keys():
            count_dict[byte] = line.count(byte)
        elif byte in count_dict.keys():
            count_dict[byte] += line.count(byte)

size = sum(count_dict.values())

for key in count_dict.keys():
    count_dict[key] = count_dict[key]/size

for k, v in count_dict.items():
    print(k, ": ", v)

test_file.close()
