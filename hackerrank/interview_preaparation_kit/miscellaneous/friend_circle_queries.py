"""
https://www.hackerrank.com/challenges/friend-circle-queries/
"""


def maxCircle_old(queries):
    """original version"""
    d = {}
    m = 1
    result = []
    queries = [(p-1, q-1) for p, q in queries]
    for p, q in queries:
        if q in d.get(p, []):
            result.append(m)
        else:
            d.setdefault(p, set([p]))
            d.setdefault(q, set([q]))
            if len(d[p]) < len(d[q]):
                p, q = q, p
            d[p] |= d[q]
            for r in d[q]:
                d[r] = d[p]
            m = max(len(d[p]), m)
            result.append(m)
    return result


def maxCircle(queries):
    """generator version"""
    d = {}
    m = 1
    queries = [(p-1, q-1) for p, q in queries]
    for p, q in queries:
        if q in d.get(p, []):
            yield m
        else:
            d.setdefault(p, set([p]))
            d.setdefault(q, set([q]))
            if len(d[p]) < len(d[q]):
                p, q = q, p
            d[p] |= d[q]
            for r in d[q]:
                d[r] = d[p]
            m = max(len(d[p]), m)
            yield m
