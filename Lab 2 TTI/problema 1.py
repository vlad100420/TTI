import numpy as np

P = np.asanyarray(list(map(float, input().split(' '))))
T = [[0.25, 0.5, 0.25],
     [0.5, 0.25, 0.25],
     [0.25, 0.25, 0.5]]
T = np.asanyarray(T)
if np.any(P < 0) or np.any(P > 1) or not np.allclose(np.sum(P), 1):
    raise Exception('P nu este valid')

P_urm = P @ np.linalg.matrix_power(T, 7)
print(f'{P_urm:.6f}')
