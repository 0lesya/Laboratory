from time import time
import os, queue, threading
from lab_6_4_2 import get_files, find_key


def find_key_second(que):
    while True:
        job = que.get()
        try:
            f = open(job, 'r', encoding='utf-8')
            if 'планеты' in f.read():
                print(job)
                pass
            f.close()
        except Exception as exc:
            pass
            #print('Не удалось прочитать файл ', str(filename) + '\n Ошибка: ', exc)
        finally:
            que.task_done()


queTemp = queue.Queue()
for file in get_files():
    queTemp.put(file)

if queTemp.qsize():
    th = threading.Thread(target=find_key_second, args=(queTemp,), daemon=True)
    start_time = time()
    th.start()
    queTemp.join()
    print("\nВремя выполнения программы с многопоточностью: ", str(time() - start_time), "\n")
start_time = time()
for file in get_files():
    find_key(file)

print("\nВремя выполнения программы без многопоточности: ", str(time()-start_time), "\n")
