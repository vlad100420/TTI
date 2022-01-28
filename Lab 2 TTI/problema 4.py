import numpy as np


def find(p: np.asanyarray, t: np.asanyarray, n: int) -> bool:
    for i in range(n):
        P_urm = p @ t
        if abs(P_urm[0] - p[0]) < 0.001:
            return True
        p = P_urm
    return False


P = []
N, K = map(int, input().split(' '))
T = np.asanyarray([list(map(float, input().split(' '))) for i in range(K)])
for i in range(K):
    P.append(1/K)
P = np.asanyarray(P)

print(find(P, T, N))
