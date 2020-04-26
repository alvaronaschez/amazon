"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2986/

Cut Off Trees for Golf Event

You are asked to cut off trees in a forest for a golf event. The forest is
represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through,
and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and
right also when standing in a point which is a tree you can decide whether or
not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's
height - always cut off the tree with lowest height first. And after cutting,
the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps
you need to walk to cut off all the trees. If you can't cut off all the trees,
output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at
least one tree needs to be cut off.

Example 1:

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6


Example 2:

Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1


Example 3:

Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in
(0,0) directly without walking.


Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9
"""
from typing import List
from collections import defaultdict
from math import inf
from copy import deepcopy


class FirstSolution:
    """
    not accepted
    timeout
    """
    @staticmethod
    def floyd_warshall(nodes, distance, copy=True):
        if copy:
            distance = deepcopy(distance)
        for k in nodes:
            for u in nodes:
                for v in nodes:
                    distance[(u, v)] = min(distance[(u, v)],
                                           distance[(u, k)] + distance[(k, v)])
        return distance

    @classmethod
    def cutOffTree(cls, forest: List[List[int]]) -> int:
        aux = [(0, (0, 0))]
        nodes = set()
        distance = defaultdict(lambda: inf)
        for i, l in enumerate(forest):
            for j, v in enumerate(l):
                if v > 1:
                    aux.append((v, (i, j)))
                if v:
                    nodes.add((i, j))
        for node in nodes:
            i, j = node
            distance[(node, node)] = 0
            for adjacent in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if adjacent in nodes:
                    distance[(node, adjacent)] = 1
        distance = cls.floyd_warshall(nodes, distance, copy=False)
        aux = sorted(aux)
        aux = [node for (_, node) in aux]
        path = [x for x in zip(aux, aux[1:])]
        result = sum([distance[x] for x in path])
        if result == inf:
            return -1
        return result


class Solution:
    @classmethod
    def cutOffTree(cls, forest: List[List[int]]) -> int:
        path = [(v, i, j) for i, row in enumerate(forest)
                for j, v in enumerate(row) if v > 1]
        path.append((0, 0, 0))
        path = sorted(path)
        path = ((x[1:], y[1:]) for x, y in zip(path, path[1:]))
        result = 0
        for start, end in path:
            x = cls.bfs(start, end, forest)
            if x == -1:
                return -1
            result += x
        return result

    @classmethod
    def bfs(cls, start, end, forest):
        open_set = [start]
        steps = 0
        closed_set = set()
        while open_set:
            aux = []
            while open_set:
                current = open_set.pop()
                if current == end:
                    return steps
                closed_set.add(current)
                for neighbor in cls.neighbors(current, forest):
                    i, j = neighbor
                    if forest[i][j] > 0 and neighbor not in closed_set:
                        closed_set.add(neighbor)
                        aux.append(neighbor)
            steps += 1
            open_set = aux
        return -1

    @staticmethod
    def neighbors(node, forest):
        i, j = node
        if i > 0:
            yield i - 1, j
        if j > 0:
            yield i, j - 1
        if i + 1 - len(forest):
            yield i + 1, j
        if j + 1 < len(forest[0]):
            yield i, j + 1
