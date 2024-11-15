from collections import deque

N, M = map(int, input().split())

d = [None] * N
# d[i]: i**2 + d[i]**2 == M
for i in range(N):
    for j in range(i, N):
        if i**2 + j**2 == M:
            d[i] = j
            d[j] = i


# BFS
todo = deque([(0, 0)])
dist = [[-1] * N for _ in range(N)]
dist[0][0] = 0
while todo:
    vi, vj = todo.popleft()
    for wi in range(N):
        dwj = d[abs(vi - wi)]
        if dwj is None:
            continue
        for sgn in [-1, 1]:
            wj = vj + sgn * dwj
            if not (0 <= wj < N):
                continue
            if dist[wi][wj] != -1:  # 既に調べた点は飛ばす
                continue
            if (vi - wi) ** 2 + (vj - wj) ** 2 == M:
                todo.append((wi, wj))
                dist[wi][wj] = dist[vi][vj] + 1

for l in dist:
    print(*l)
