"""
https://www.hackerrank.com/challenges/maximum-xor/

works with Pypy3, with Python3 4 test cases fail
"""
from itertools import chain
from math import ceil, log


class Trie:
    """https://en.wikipedia.org/wiki/Trie"""
    class Node:
        def __init__(self):
            self.children = {}
            self.value = None

    def __init__(self, fmt: int = 30):
        self.fmt = '0{}b'.format(fmt)
        self.root = self.Node()

    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = self.Node()
            node = node.children[char]
        node.value = value

    def _gen(self, n):
        return (int(x) for x in format(n, self.fmt))

    def add_int(self, n):
        gen = self._gen(n)
        self.insert(gen, n)

    def max_xor(self, n):
        node = self.root
        gen = self._gen(n)
        for b in gen:
            if b ^ 1 in node.children:
                node = node.children[b ^ 1]
            else:
                node = node.children[b]
        return node.value


# Complete the maxXor function below.
def maxXor(arr, queries):
    m = max(chain(arr, queries))
    fmt = ceil(log(m, 2))
    # build the trie
    t = Trie(fmt)
    for n in arr:
        t.add_int(n)
    for q in queries:
        yield t.max_xor(q) ^ q
