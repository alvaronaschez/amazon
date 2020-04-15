from itertools import count


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_lists = [[] for _ in range(n)]

    def connect(self, x, y):
        self.adj_lists[x].append(y)
        self.adj_lists[y].append(x)

    def distances(self, s):
        distances = [-1]*self.n
        distances[s] = 0
        open_set = [s]
        closed_set = set()
        for c in count(1):
            new_open_set = []
            for n in open_set:
                for m in self.adj_lists[n]:
                    if m not in closed_set:
                        distances[m] = c
                        closed_set.add(m)
                        new_open_set.append(m)
            open_set = new_open_set
            if not open_set:
                return distances

    def find_all_distances(self, s):
        result = (
            6*d if d > 0 else d
            for i, d in enumerate(self.distances(s))
            if i != s
        )
        print(*result)


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)
    s = int(input())
    graph.find_all_distances(s-1)
