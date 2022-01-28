import numpy as np
from typing import Union


# Ex1
def p1(a: str, p: float) -> Union[float, str]:
    if np.any(p < 0) or np.any(p > 1):
        return 'Date de intrare invalide!'
    elif (a != 'CBS') and (a != 'CBA'):
        return 'Date de intrare invalide!'
    if a == 'CBS':
        if p == 0 or p == 1:
            c = 1
        else:
            c = (1 + p * np.log2(p) + (1 - p) * np.log2(1 - p))
    else:
        c = 1 - p
    return c


# Ex2
def p2(lp: list[float]) -> Union[list[float], str]:
    result = []
    for x in lp:
        if np.any(x < 0) or np.any(x > 1):
            return 'Date de intrare invalide!'
        else:
            if x == 0:
                c = np.log2(3)
            elif x == 1:
                c = np.log2(3) - 1
            else:
                c = np.log2(3) + (1 - x) * np.log2(1 - x) + x * np.log2(x / 2)
            result.append(c)
    return result


# Ex3
def trans(a: float):
    if a == 0:
        return 0
    else:
        I = - (a / 2) * np.log2(a / 2) - (1 - (a / 2)) * np.log2(1 - (a / 2)) - a
    return I


def p3(a: float):
    I = trans(a)
    C = trans(2 / 5)

    return [I, C, 2 / 5]


# Ex4
def p4(Px: float, N: float, W: float) -> float:
    C = W * np.log2(1 + (Px / N))
    return C
