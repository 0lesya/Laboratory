import numpy as np
N = int(input())
M = int(input())
matrixA = np.random.randint(0, M, (M, M))
for _ in range(N-1):
    matrixB = np.random.randint(0, M, (M, M))
    matrixA = matrixA.dot(matrixB)
for i in matrixA:
    print(i)
    print('')
