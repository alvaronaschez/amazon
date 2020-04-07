def criticalRouters(numRouters, numLinks, links):
    if numRouters == 0:
        return []
    if numRouters == 1:
        return [1]
    if numLinks == 0:
        return list(range(1, numLinks))
    d = {}
    for link in links:
        a, b = link
        d.setdefault(a, []).append(b)
        d.setdefault(b, []).append(a)

    def foo(excluded):
        closed_set = set()
        open_set = [1] if excluded != 1 else [2]
        while open_set:
            node = open_set.pop()
            if node == excluded:
                continue
            closed_set.add(node)
            if len(closed_set) == numRouters-1:
                return True
            for child in d[node]:
                if child not in closed_set and child != excluded:
                    open_set.append(child)
        return len(closed_set) == numRouters-1

    result = []
    for node in range(1, numRouters+1):
        if not foo(node):
            result.append(node)

    return sorted(result)
