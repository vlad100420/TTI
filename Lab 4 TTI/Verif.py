import heapq
import math as mt
from typing import List


class Node:
    def __init__(self, p, s):
        self.left = None
        self.right = None
        self.prob = p
        self.symbol = s

    def __lt__(self, other):
        return self.prob < other.prob

    def __repr__(self):
        return "Node({}, {}, {})".format(repr([self.prob, self.symbol]), repr(self.left), repr(self.right))


def HuffmanTree(SP):
    pq = []
    for symbol, prob in SP.items():
        pq.append(Node(prob, symbol))
    heapq.heapify(pq)

    while len(pq) > 1:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        top = Node(n1.prob + n2.prob, n1.symbol + n2.symbol)
        top.left = n1
        top.right = n2
        heapq.heappush(pq, top)

    return pq


def encode(dic_code, root, code):
    if root.left is None and root.right is None:
        dic_code[root.symbol] = code
    else:
        encode(dic_code, root.left, code + '0')
        encode(dic_code, root.right, code + '1')


def p3(text: str) -> List[int]:
    s = []
    p = []
    for litere in text:
        if (litere in s):
            pass
        else:
            s.append(litere)

    for i in s:
        p.append(text.count(i) / len(text))
    SP = dict((s[i], p[i]) for i in range(len(s)))
    dic_code = dict((s[i], '') for i in range(len(s)))
    QP = HuffmanTree(SP)
    encode(dic_code=dic_code, root=QP[0], code='')
    sumi = 0
    for i in text:
        sumi += len(dic_code[i])

    logul = mt.ceil(mt.log2(len(s))) * len(text)
    return ([sumi, int(logul)])


print(p3("ana are mere"))
