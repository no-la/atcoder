import itertools
from collections import defaultdict
from collections import deque


memo = defaultdict(lambda: -1)


def f(vals: tuple):
    if vals in memo:
        return memo[vals]
    rev = 0
    for v in vals:
        rev ^= v
    memo[vals] = rev
    return rev


N = int(input())
A = list(map(int, input().split()))

ans = set()
ans.add(f(tuple(A)))

# DFS

todo = deque([tuple(sorted(A))])
seen = defaultdict(lambda: False)
seen[todo[0]] = True
while todo:
    v = todo.pop()
    for l in itertools.combinations(v, 2):
        a, b = l
        w = []
        a_seen, b_seen = False, False
        for x in v:
            if x == a and not a_seen:
                a_seen = True
            elif x == b and not b_seen:
                b_seen = True
            else:
                w.append(x)
        w.append(a + b)
        w = tuple(sorted(w))

        if seen[w]:
            continue
        todo.append(w)
        seen[w] = True
        ans.add(f(w))

print(len(ans))
