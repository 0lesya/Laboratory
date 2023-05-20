from math import sqrt
from time import time
import multiprocessing


def matrix_count(n, p, q):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = sqrt((q[j]-p[i])**2)


if __name__ == '__main__':
    N = 5000
    P = list(range(1, N+1))
    Q = list(range(6, N+7))

    start_time = time()
    matrix_count(N, P, Q)
    print("Время выполнения программы без многопоточности: ", str(time()-start_time))

    start_time = time()
    t1 = multiprocessing.Process(target=matrix_count, args=(N, P, Q, ))
    t1.start()
    t1.join()
    print("Время выполнения программы c многопоточностью: ", str(time()-start_time))
