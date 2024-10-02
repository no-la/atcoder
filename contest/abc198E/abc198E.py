N = int(input())
C = list(map(int, input().split()))
d = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)
M = 10**5

import sys

sys.setrecursionlimit(10**6)


seen = [False] * N
color_count = [0] * (M + 1)
ans = []


def f(v):
    if color_count[C[v]] == 0:
        ans.append(v)
    color_count[C[v]] += 1
    for w in d[v]:
        if seen[w]:
            continue
        seen[w] = True
        f(w)

    color_count[C[v]] -= 1


seen[0] = True
f(0)
print(*sorted(map(lambda x: x + 1, ans)), sep="\n")
