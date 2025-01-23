N, M = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

d = [[] for _ in range(N)]
for a in A:
    d[a].append(a + 1)
    d[a + 1].append(a)

ans = []

# DFS
from collections import deque

seen = [False] * N
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    todo = deque([i])
    temp = [i]
    while todo:
        v = todo.pop()
        for w in d[v]:
            if seen[w]:
                continue
            todo.append(w)
            seen[w] = True
            temp.append(w)
    ans += sorted(map(lambda x: x + 1, temp), reverse=True)

print(*ans)
