import numpy as np

N, K = map(int, input().split(' '))
P = np.asanyarray(list(map(float, input().split(' '))))
T = np.asanyarray([list(map(float, input().split(' '))) for i in range(K)])
print(N, K)
print(P)
print(T)


