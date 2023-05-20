import os

archive_name = 'archive.NIYSOI'
archive = open('archive.NIYSOI', 'r', encoding='utf-8') #открытие архива на чтение
sign = "".join([hex(ord(i))[2:] for i in os.path.splitext('archive.NIYSOI')[-1]][1:])
zag = archive.readlines() #сохраняем в список строки по очереди
signature = zag[0][:(len(zag[0])-1)].replace(' ', '') #берем первую строку, в которой написана сигнатура
filenames = zag[4].split()
lens = zag[5].split()
if sign == signature:
    algorithms = [int(i) for i in zag[2][:(len(zag[2])-1)].replace(' ', '')] #берем 3 строку, в которой хранится алгоритм
    if sum(algorithms) == 0:
        k=6
        for i in range(len(filenames)):
            filename = filenames[i][2:len(filenames[i])-1]
            filename = bytes.fromhex(filename).decode('utf-8')
            new_file = open(filename, mode='w+', encoding='utf-8')
            for line in zag[k:k+int(lens[i])+1]:
                new_file.write((bytes.fromhex(line)).decode('utf-8'))
            new_file.close()
            k += int(lens[i])+1

archive.close()
