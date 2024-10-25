N = int(input())
d = [tuple(map(int, input().split())) for _ in range(N)]
from collections import defaultdict

A = defaultdict(int)
for xy in d:
    A[xy] = 1

# DFS
from collections import deque

ans = 0
seen = set()
for s in range(N):
    if d[s] in seen:
        continue
    seen.add(d[s])
    ans += 1
    todo = deque([d[s]])
    while todo:
        vi, vj = todo.pop()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == -j:
                    continue
                w = (vi + i, vj + j)
                if w in seen:
                    continue
                if A[w]:
                    todo.append(w)
                    seen.add(w)
# print(A)
print(ans)
