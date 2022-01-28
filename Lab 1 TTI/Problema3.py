import numpy as np


def normalizeaza(vector: np.ndarray) -> np.ndarray:
    new_vec = np.random.standard_normal(vector.shape)
    return new_vec
