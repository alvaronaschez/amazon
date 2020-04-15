"""
https://www.hackerrank.com/challenges/find-the-nearest-clone/

 Complete the findShortest function below.


 For the weighted graph, <name>:

 1. The number of nodes is <name>_nodes.
 2. The number of edges is <name>_edges.
 3. An edge exists between <name>_from[i] to <name>_to[i].
"""
from itertools import count


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # from 1-based indexing to 0-based indexing
    graph_from = [x-1 for x in graph_from]
    graph_to = [x-1 for x in graph_to]
    ids = [x-1 for x in ids]
    val -= 1
    # build the adjacency lists
    adj_lists = tuple([] for _ in range(graph_nodes))
    for i, j in zip(graph_from, graph_to):
        adj_lists[i].append(j)
        adj_lists[j].append(i)
    # build a set with the nodes of the target color
    targets = {i for i, v in enumerate(ids) if v == val}
    # build open and closed sets
    open_sets = [[n] for n in range(graph_nodes)]
    closed_sets = tuple(set() for _ in range(graph_nodes))
    # iterate
    for c in count():
        # parallel search
        number_of_closed_sets = 0
        for n in targets:
            new_open_set = []
            for m in open_sets[n]:
                if m not in closed_sets[n]:
                    if m != n and m in targets:
                        return c
                    closed_sets[n].add(m)
                    for p in adj_lists[m]:
                        if p not in closed_sets[n]:
                            new_open_set.append(p)
            if not new_open_set:
                number_of_closed_sets += 1
            open_sets[n] = new_open_set
        if number_of_closed_sets == len(targets):
            return -1
