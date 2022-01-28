import numpy as np


def grad(p):
    # np.polyld considera putere maxima pe prima pozitie in vector
    p = np.poly1d(np.flipud(p))
    return p.order


def X(m):
    # reprezinta X^m --> [ 0 0 ... 0 1]
    X = np.zeros(m + 1, dtype=int)
    X[m] = 1
    return X


def cautare_dict(dictionary, cod_cautat):
    for lit, cod in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        # print("cod", cod)
        # print("cod_cautat", cod_cautat)
        if np.allclose(cod, cod_cautat):
            return lit

    return np.array([-1, -1, -1, -1])


class GF2m:
    def __init__(self, g):
        self.g = g
        self.m = grad(g)
        self.n = np.power(2, self.m) - 1
        self.k = self.n - self.m
        self.p = self.adunare_polinoame(X(self.n), X(0))  # X^n + 1
        (self.h, _) = self.divizare_polinoame(self.p, self.g)

    def adunare_polinoame(self, a, b):
        s = np.mod(np.flipud(np.polyadd(np.flipud(a), np.flipud(b))), 2)
        return s.astype(int)

    def inmultire_polinoame(self, a, b):
        p = np.mod(np.flipud(np.polymul(np.flipud(a), np.flipud(b))), 2)
        # In algebra polinoamelor modulo (X^n + 1), X^n = X^0, X^(n+1) = X^1, ...
        # s.a.m.d

        if grad(p) > self.n - 1:
            for i in range(self.n, grad(p) + 1):
                p[i - self.n] = np.mod(p[i - self.n] + p[i], 2)
                p[i] = 0

        p = p[0:grad(p) + 1]

        return p

    def divizare_polinoame(self, a, b):
        # np.flipud(a)
        (cat, rest) = np.polydiv(np.flipud(a), np.flipud(b))
        cat = np.mod(np.flipud(cat), 2)
        rest = np.mod(np.flipud(rest), 2)
        return cat.astype(int), rest.astype(int)

    def gasire_polinomXk(self, rest):
        for i in range(0, 7):
            (c, r) = self.divizare_polinoame(X(i), self.g)
            rest = self.adunare_polinoame(rest, np.zeros(7))
            r = self.adunare_polinoame(r, np.zeros(7))
            if np.allclose(rest, r):
                return X(i)

        return np.array([0])


def g1_encode(text: str) -> np.ndarray:
    g = np.array([1, 1, 0, 1])  # 1 + X + X^3
    gf2m = GF2m(g)
    alfabet = {
        'A': np.array([0, 0, 0, 0]),
        'B': np.array([0, 0, 0, 1]),
        'C': np.array([0, 0, 1, 0]),
        'D': np.array([0, 0, 1, 1]),
        'E': np.array([0, 1, 0, 0]),
        'F': np.array([0, 1, 0, 1]),
        'G': np.array([0, 1, 1, 0]),
        'H': np.array([0, 1, 1, 1]),
        'I': np.array([1, 0, 0, 0]),
        'J': np.array([1, 0, 0, 1]),
        'K': np.array([1, 0, 1, 0]),
        'L': np.array([1, 0, 1, 1]),
        'M': np.array([1, 1, 0, 0]),
        'N': np.array([1, 1, 0, 1]),
        'O': np.array([1, 1, 1, 0]),
        'P': np.array([1, 1, 1, 1]),
    }

    M = np.zeros((len(text), 7), dtype=int)
    j = 0
    for lit in text:
        xi = gf2m.inmultire_polinoame(X(3), np.flipud(alfabet[lit]))
        (c1, r1) = gf2m.divizare_polinoame(xi, g)
        M[j] = gf2m.adunare_polinoame(gf2m.adunare_polinoame(r1, xi), np.zeros(7))
        j = j + 1

    return M


def g1_decode(code_matrix: np.ndarray) -> str:
    g = np.array([1, 1, 0, 1])  # 1 + X + X^3
    gf2m = GF2m(g)
    alfabet = {
        'A': np.array([0, 0, 0, 0]),
        'B': np.array([0, 0, 0, 1]),
        'C': np.array([0, 0, 1, 0]),
        'D': np.array([0, 0, 1, 1]),
        'E': np.array([0, 1, 0, 0]),
        'F': np.array([0, 1, 0, 1]),
        'G': np.array([0, 1, 1, 0]),
        'H': np.array([0, 1, 1, 1]),
        'I': np.array([1, 0, 0, 0]),
        'J': np.array([1, 0, 0, 1]),
        'K': np.array([1, 0, 1, 0]),
        'L': np.array([1, 0, 1, 1]),
        'M': np.array([1, 1, 0, 0]),
        'N': np.array([1, 1, 0, 1]),
        'O': np.array([1, 1, 1, 0]),
        'P': np.array([1, 1, 1, 1]),
    }

    # M = np.zeros((len(text), 7), dtype=int)
    dtext = ''
    j = 0
    for code in code_matrix:
        (c1, r1) = gf2m.divizare_polinoame(code, g)
        # z = r1
        v = gf2m.adunare_polinoame(code, gf2m.gasire_polinomXk(r1))
        (c2, r2) = gf2m.divizare_polinoame(v, g)

        (inf, x) = np.array_split(np.flipud(v), 2)
        dtext = dtext + cautare_dict(alfabet, inf)

    return dtext
