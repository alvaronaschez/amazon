"""
https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/
"""

# Complete the maxRegion function below.


def maxRegion(grid):
    filled_cells = set()
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value:
                filled_cells.add((i, j))
    result = 0
    while filled_cells:
        open_set = {filled_cells.pop()}
        acc = 1
        while open_set:
            p, k = open_set.pop()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (p+i, k+j) in filled_cells:
                        open_set.add((p+i, k+j))
                        acc += 1
                        filled_cells.difference_update({(p+i, k+j)})
        result = max(result, acc)
    return result


assert 10 == maxRegion([
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0],
])
