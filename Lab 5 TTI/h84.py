import numpy as np
import random


class codH84():
    def __init__(self):
        self.n = 8
        self.k = 4
        self.m = self.n - self.k
        self.H = np.array([[0, 0, 0, 1, 1, 1, 1, 0],
                           [0, 1, 1, 0, 0, 1, 1, 0],
                           [1, 0, 1, 0, 1, 0, 1, 0],
                           [1, 1, 1, 1, 1, 1, 1, 1]])


    def __repr__(self):
        return'Matricea de control pentru codul H(3,1):\n{}'.format(repr(self.H))

    def codare(self,i):
        [i3, i5, i6, i7]=i
        c1=i3+i5+i7
        c2=i3+i6+i7
        c4=i5+i6+i7
        c8 = i3+i5+i6
        return np.array([c1,c2,i3,c4,i5,i6,i7,c8])

    def detectie_erori(self, v_rec):
        z = np.mod(np.matmul(self.H, v_rec), 2)
        if z[0]+z[1]+z[2]+z[3] == 0:
            return 0
        elif z[3] == 1:
            return 1
        else:
            return 2
    def corectie_erori(self, v_rec):
        z=np.mod(np.matmul(self.H,v_rec),2)
        if(z==np.zeros(shape=(self.m,))).all():
            return v_rec
        else:
            cuvant_eroare_estimat=np.zeros(shape=(self.n,),dtype=int)
            z=np.delete(z,-1)
            pozitie_eroare_estimata = bin2dec(z)
            cuvant_eroare_estimat[pozitie_eroare_estimata-1]=1
            v_corectat=np.mod(v_rec+cuvant_eroare_estimat,2)
            return v_corectat


def bin2dec(a):
    b = 0
    for p in range(len(a)):
        b += a[-p-1] * (2**p)
    return np.int32(b)


def h84_encode(text:str) -> np.ndarray :
    alfabet = {
        'A': np.array([0,0,0,1]),
        'B': np.array([0,0,1,0]),
        'C': np.array([0,0,1,1]),
        'D': np.array([0,1,0,0]),
        'E': np.array([0,1,0,1]),
        'F': np.array([0,1,1,0]),
        'G': np.array([0,1,1,1]),
        'H': np.array([1,0,0,0]),
        'I': np.array([1,0,0,1]),
        'J': np.array([1,0,1,0]),
        'K': np.array([1,0,1,1]),
        'L': np.array([1,1,0,0]),
        'M': np.array([1,1,0,1]),
        'N': np.array([1,1,1,0]),
        'O': np.array([1,1,1,1]),
        'P': np.array([0,0,0,0])
    }
    cod = codH84()
    resp = np.zeros([len(text),8])
    i = 0
    for el in text:
        info = alfabet[el]
        v = cod.codare(info)
        resp[i] = v
        i = i+1
    return resp

def h84_decode(code_matrix: np.ndarray) -> str :
    alfabet = {
        'A': np.array([0, 0, 0, 1]),
        'B': np.array([0, 0, 1, 0]),
        'C': np.array([0, 0, 1, 1]),
        'D': np.array([0, 1, 0, 0]),
        'E': np.array([0, 1, 0, 1]),
        'F': np.array([0, 1, 1, 0]),
        'G': np.array([0, 1, 1, 1]),
        'H': np.array([1, 0, 0, 0]),
        'I': np.array([1, 0, 0, 1]),
        'J': np.array([1, 0, 1, 0]),
        'K': np.array([1, 0, 1, 1]),
        'L': np.array([1, 1, 0, 0]),
        'M': np.array([1, 1, 0, 1]),
        'N': np.array([1, 1, 1, 0]),
        'O': np.array([1, 1, 1, 1]),
        'P': np.array([0, 0, 0, 0])
    }
    cod = codH84()
    resp = ''
    for el in code_matrix:
        if cod.detectie_erori(el) == 2:
            resp += '*'
        else:
            corectat = cod.corectie_erori(el)
            info = [int(corectat[2]), int(corectat[4]), int(corectat[5]), int(corectat[6])]
            for el in alfabet:
                if np.array_equal(alfabet[el], info):
                    resp = resp + el
    return resp


# Test 1

code_matrix = h84_encode('KEEIBNF')
error_matrix = np.asanyarray([[0, 0, 1, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0, 1],
                              [0, 0, 0, 0, 0, 0, 0, 1],
                              [0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 0]])
code_matrix = (code_matrix + error_matrix) % 2
text = h84_decode(code_matrix)
print(text == '*EE*BNF')

# Test 2
"""
code_matrix = h84_encode('FGBPGDNGGO')
error_matrix = np.asanyarray([[1, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 0],
                              [1, 0, 0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 1, 1],
                              [1, 0, 0, 0, 0, 0, 0, 1],
                              [0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 1]])
code_matrix = (code_matrix + error_matrix) % 2
text = h84_decode(code_matrix)
print(text == 'FGBP*D**G*')"""