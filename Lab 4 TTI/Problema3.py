import heapq
import math as mt


class Node:
    def __init__(self, p, s):
        self.left = None
        self.right = None
        self.prob = p
        self.symbol = s

    def __lt__(self, other):
        return self.prob < other.prob

    def __repr__(self):
        return "Node({}, {}, {}".format(repr([self.prob, self.symbol]), repr(self.left), repr(self.right))


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


def p1(text) -> list[float]:
    total = 0
    S = list(text)
    P = []
    for c in text:
        P.append(text.count(c) / len(text))
    dic_code = dict((S[i], ' ') for i in range(len(S)))
    SP = dict((S[i], P[i]) for i in range(len(S)))
    PQ = HuffmanTree(SP)
    encode(dic_code=dic_code, root=PQ[0], code='')
    for s in S:
        total += len(dic_code[s])
    codare_fixa = mt.ceil(mt.log(len(SP), 2)) * len(text)
    return [total, codare_fixa]
