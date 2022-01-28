import numpy as np

P = np.asanyarray(list(map(float, input().split(' '))))
Val = []
T = [[0.01, 0.98, 0.01],
     [0.98, 0.01, 0.01],
     [0.01, 0.01, 0.98]]
T = np.asanyarray(T)
if np.any(P < 0) or np.any(P > 1) or not np.allclose(np.sum(P), 1):
    raise Exception('P nu este valid')

for i in range(8):
    Val.append(P[2])
    P = P @ T
print(Val)
