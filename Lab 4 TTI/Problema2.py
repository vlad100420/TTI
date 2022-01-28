import heapq
import math as mt


class Node:
    def __init__(self, p, s):
        self.left = None
        self.mid = None
        self.right = None
        self.prob = p
        self.symbol = s

    def __lt__(self, other):
        return self.prob < other.prob

    def __repr__(self):
        return "Node({}, {}, {}".format(repr([self.prob, self.symbol]), repr(self.left), repr(self.mid),
                                        repr(self.right))


def HuffmanTree(SP):
    pq = []
    for symbol, prob in SP.items():
        pq.append(Node(prob, symbol))
    heapq.heapify(pq)
    if len(SP.keys()) % 2 == 0:
        heapq.heappush(pq, Node(p=0, s=f's{len(SP.keys())+1}'))

    while len(pq) > 1:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        n3 = heapq.heappop(pq)
        top = Node(n1.prob + n2.prob + n3.prob, n1.symbol + n2.symbol + n3.symbol)
        top.left = n1
        top.mid = n2
        top.right = n3
        heapq.heappush(pq, top)
    return pq


def encode(dic_code, root, code):
    if root.left is None and root.right is None:
        dic_code[root.symbol] = code
    else:
        encode(dic_code, root.left, code + 1)
        encode(dic_code, root.mid, code + 1)
        encode(dic_code, root.right, code + 1)


def p1(S, P) -> list[float]:
    lmed = 0
    dic_code = dict((S[i], ' ') for i in range(len(S)))
    SP = dict((S[i], P[i]) for i in range(len(S)))
    PQ = HuffmanTree(SP)
    encode(dic_code=dic_code, root=PQ[0], code=0)
    lungimi = []
    for s in dic_code:
        lungimi.append(dic_code[s])
    for (prob, lungime) in zip(P, lungimi):
        lmed += lungime * prob
    return [lmed]
