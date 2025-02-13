import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    d[b].append(a)
    deg[a] += 1
    deg[b] += 1

leaf = deg.index(1)
ans = [set(), set()]
# DFS
from collections import deque

for i in range(2):
    todo = deque([(leaf, i)])
    seen = [False] * N
    seen[leaf] = True
    while todo and len(ans[i]) < N // 2:
        v, a = todo.pop()
        if a:
            ans[i].add(v + 1)
        for w in d[v]:
            if seen[w]:
                continue
            seen[w] = True
            todo.append((w, a ^ 1))

    if len(ans[i]) == N // 2:
        print(*ans[i])
        exit()
