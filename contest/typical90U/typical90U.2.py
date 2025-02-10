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
    todo = deque([(i,)])
    while todo:
        v, *others = todo.pop()
        # print(v, others)
        if v == -1:
            v = others[0]
            query.append(v)
            continue

        if seen[v]:
            continue
        seen[v] = True
        todo.append((-1, v))
        for w in E[v]:
            if seen[w]:
                continue
            todo.append((w,))


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
