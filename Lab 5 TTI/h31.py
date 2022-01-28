import numpy as np
import random


class codH31:
    def __init__(self):
        self.n = 3
        self.k = 1
        self.m = self.n - self.k
        self.H = ([0, 1, 1],
                  [1, 0, 1])

    def __repr__(self):
        return 'Matricea de control pentru codul H(3,1):\n' \
               '{}'.format(repr(self.H))

    def codare(self, i):
        i3 = i
        c1 = i3 % 2
        c2 = i3 % 2
        return np.array([c1, c2, i3])

    def detectie_erori(self, v_rec):
        z = np.mod(np.matmul(self.H, v_rec), 2)
        return (z == np.zeros(shape=(self.m,))).all()

    def corectie_erori(self,v_rec):
        z = np.mod(np.matmul(self.H, v_rec), 2)
        if (z == np.zeros(shape=(self.m,))).all():
            return v_rec
        else:
            cuvant_eroare_estimat = np.zeros(shape=(self.n,), dtype=int)
            pozitie_eroare_estimata = bin2dec(z)
            cuvant_eroare_estimat[pozitie_eroare_estimata-1] = 1
            v_corectat = np.mod(v_rec + cuvant_eroare_estimat, 2)
            return v_corectat


def bin2dec(a):
    b = 0
    for p in range(len(a)):
        b += a[-p-1]*(2**p)
    return int(b)


def transmitere_canal(v, e):
    cuvant_eroare = np.zeros(shape=(len(v),), dtype=int)
    pozitie_eronata = random.sample(range(len(v)), k=e)
    cuvant_eroare[pozitie_eronata] = 1
    v_rec = np.mod(v + cuvant_eroare, 2)
    return v_rec


cod = codH31()


def h31_encode(text : str):
    i1 = []
    for c in text:
        i1.append(int(c))
    code_matrix = np.zeros([len(text), 3])
    ctr = 0
    for i in i1:
        code_matrix[ctr,:] = cod.codare(i)
        ctr += 1
    return code_matrix


def h31_decode(code_matrix):
    e = 0
    i_decodare=''
    for i in range(len(code_matrix)):
        v_rec = transmitere_canal(code_matrix[i,:], e)
        v_corectat = cod.corectie_erori(v_rec)
        i_decodare = i_decodare+str(int(v_corectat[2]))
    return i_decodare


#i = '0011011011'
#v = h31_encode(i)
#print(v)
#print(h31_decode(v))
"""
# Test 1
code_matrix = h31_encode('0011011011')
error_matrix = 0
code_matrix = (code_matrix + error_matrix) % 2
text = h31_decode(code_matrix)
print(text == '0011011011')"""
"""
# Test 2
code_matrix = h31_encode('101001')
error_matrix = np.asanyarray([[0, 1, 0],
                              [1, 0, 0],
                              [0, 0, 0],
                              [0, 0, 1],
                              [0, 0, 0],
                              [0, 1, 0]])
code_matrix = (code_matrix + error_matrix) % 2
text = h31_decode(code_matrix)
print(text == '101001')"""

# Test 3
"""
code_matrix = h31_encode('0100101')
error_matrix = np.asanyarray([[1, 0, 0],
                              [0, 0, 1],
                              [0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 1],
                              [0, 1, 0],
                              [0, 0, 1]])
code_matrix += error_matrix
text = h31_decode(code_matrix)
print(text == '0100101')"""

# Test 4
"""
code_matrix = h31_encode('0111001')
error_matrix = np.asanyarray([[0, 1, 0],
                              [0, 0, 1],
                              [0, 0, 1],
                              [1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1],
                              [0, 0, 1]])
code_matrix = (code_matrix + error_matrix) % 2
text = h31_decode(code_matrix)
print(text == '0111001')"""
