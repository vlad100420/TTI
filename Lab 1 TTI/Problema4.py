import numpy as np


def vector_in_matrice(matrice: np.ndarray, vector: np.ndarray) -> bool:
    for i in matrice:
        if np.array_equal(i, vector):
            return True
            break
    return False
