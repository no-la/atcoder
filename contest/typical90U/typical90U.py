import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
E = [[] for _ in range(N)]
reversed_E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    E[a].append(b)
    reversed_E[b].append(a)

# 連結成分ごとに強連結成分分解
# DFS
from collections import deque

ans = 0

query = []
seen = [False] * N
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    todo = deque([(-1, None, i), (i,)])
    while todo:
        v, *others = todo.pop()
        # print(v, others)
        if v == -1:
            v, w = others
            query.append(w)
            continue
        for w in E[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w))
            todo.append((w,))
            seen[w] = True


# print(query)

seen = [False] * N
for v in query[::-1]:
    if seen[v]:
        continue
    seen[v] = True
    todo = [v]
    size = 1
    while todo:
        v = todo.pop()
        for w in reversed_E[v]:
            if seen[w]:
                continue
            seen[w] = True
            todo.append(w)
            size += 1
    ans += size * (size - 1) // 2

print(ans)
