import numpy as np

p = float(input())
P = [1, 0, 0]
T = [[p, 1-(2*p), p],
     [1-(2*p), p, p],
     [p, p, 1-(2*p)]]
T = np.asanyarray(T)
P = np.asanyarray(P)
if np.any(T < 0) or np.any(T > 1) or not np.allclose(np.sum(T, axis=1), 1):
    raise Exception('T nu este valid')
P_5 = P @ np.linalg.matrix_power(T, 5)
print(P_5[1])
