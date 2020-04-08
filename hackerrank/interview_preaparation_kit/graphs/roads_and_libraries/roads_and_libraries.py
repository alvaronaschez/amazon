"""
https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs
"""

from itertools import compress


def group_cost(n, c_lib, c_road):
    """
    return the cost for a group of n cities

    answer gonna be:
    return c1 if c_road < c_lib else c2
    do the math!
    """
    # buy a library and n-1 roads
    c1 = c_lib + (n-1)*c_road
    # buy n libraries
    c2 = n * c_lib
    return min(c1, c2)


def roads_and_libraries(n, c_lib, c_road, roads):
    # transform 1-based indexing into 0-based indexing
    roads = ((c1-1, c2-1) for c1, c2 in roads)
    # construct a list of adjacency lists for each city
    adjacency_lists = [[] for _ in range(n)]
    for city1, city2 in roads:
        adjacency_lists[city1].append(city2)
        adjacency_lists[city2].append(city1)

    closed_set = set()
    open_set = set(range(n))
    result = 0
    while open_set:
        city = open_set.pop()
        closed_set.add(city)
        open_stack = adjacency_lists[city][:]
        count = 1
        while open_stack:
            city = open_stack.pop()
            if city not in closed_set:
                open_set.difference_update({city})
                closed_set.add(city)
                count += 1
                for adj_city in adjacency_lists[city]:
                    if adj_city not in closed_set:
                        open_stack.append(adj_city)
        result += group_cost(count, c_lib, c_road)
    return result
