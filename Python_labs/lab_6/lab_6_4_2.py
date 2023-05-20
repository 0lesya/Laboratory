import threading, os
from time import time


def find_key(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        if 'планеты' in f.read():
            print(filename)
            pass
        f.close()
    except Exception as exc:
        pass
        #print('Не удалось прочитать файл ', str(filename) + '\n Ошибка: ', exc)


def get_files():
    list_files = []
    for files in os.walk(os.getcwd()):
        for iter_file in files[2]:
            if iter_file.endswith(".txt"):
                list_files.append(os.path.join(files[0], iter_file))
    return list_files


threads = [threading.Thread(target=find_key, args=(elem,)) for elem in get_files()]
start_time = time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("\nВремя выполнения программы с многопоточностью: ", str(time() - start_time), "\n")

start_time = time()
for file in get_files():
    find_key(file)

print("\nВремя выполнения программы без многопоточности: ", str(time()-start_time), "\n")
