N, M = map(int, input().split())
d = [[] for _ in range(N)]
indeg = [0] * N
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    d[x].append(y)
    indeg[y] += 1

# トポロジカルソート
# DFS
from collections import deque

todo = deque([i for i in range(N) if indeg[i] == 0])
indeg_copy = indeg.copy()
S = []
while todo:
    v = todo.pop()
    for w in d[v]:
        indeg_copy[w] -= 1
        if indeg_copy[w] == 0:
            todo.append(w)
    S.append(v)

# print(S)

dp = [0] * N
# dp[i]: iを終点にしたときの最大値

for x in S:
    for y in d[x]:
        dp[y] = max(dp[y], dp[x] + 1)

print(max(dp))
