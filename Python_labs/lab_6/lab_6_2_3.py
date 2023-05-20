import threading
import os
from threading import Thread, Event
import time

# Основная задача событий - взаимодействие между потоками через механизм оповещения.
# Объект класса Event управляет внутренним флагом, который сбрасывается с помощью метода clear().
# И устанавливается методом set().

# is_set() - возвращает true если флаг находится в взведенном состоянии.
# set() - переводит флаг в взведенное состояние
# clear() - переводит флаг в сброшенное состояние
# wait() - блокирует вызвавший данный метод поток если флаг находится в сброшенном состоянии.


event = Event()


def wait_event():
    event.wait()  # Ожидаем event.set()
    print('event.set() вызван')
    some_calculation = len(list(os.walk(os.getcwd())))
    print("Файлов в папке: ", str(some_calculation))


t1 = Thread(name='blocking', target=wait_event)

t1.start()

print('ожидание перед вызовом Event.set()')
time.sleep(2)
event.set()
event.clear()
