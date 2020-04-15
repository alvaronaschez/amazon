import unittest
from math import inf
from heapq import heapify, heappop, heappush
from collections import namedtuple

Edge = namedtuple('Edge', ['cost', 'start', 'end'])


def dijkstra(vertices, start, end, directed=True):
    # build the adjacency list
    adjacency_lists = {}
    for n, m, cost in vertices:
        adjacency_lists.setdefault(n, []).append(Edge(cost, n, m))
        if not directed:
            adjacency_lists.setdefault(m, []).append(Edge(cost, m, n))

    # heapify transforms its input list into a heap in linear time
    # that is done in-place, so lets use a copy better
    open_set = adjacency_lists[start][:]
    heapify(open_set)
    closed_set = set(start)
    predecessor = {start: None}

    while open_set:
        edge = heappop(open_set)
        if edge.end in closed_set:
            continue
        closed_set.add(edge.end)
        predecessor[edge.end] = edge.start
        if edge.end == end:
            break
        for vertex in adjacency_lists.get(edge.end, []):
            heappush(open_set, vertex)

    # build the result
    if end not in predecessor:
        return None
    path = []
    pred = end
    while pred:
        path.append(pred)
        pred = predecessor[pred]
    return list(reversed(path))


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        vertices = ([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
                     ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
                     ("e", "f", 9)])
        result = dijkstra(vertices, "a", "e")
        expected_result = ['a', 'c', 'd', 'e']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
