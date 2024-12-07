H, W, D = map(int, input().split())
S = [input() for _ in range(H)]

start = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            start.append((i, j))


# BFS
from collections import deque

todo = deque(start)
dist = [[-1] * W for _ in range(H)]
for i, j in start:
    dist[i][j] = 0
while todo:
    vi, vj = todo.popleft()
    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        wi, wj = vi + di, vj + dj
        if not (0 <= wi < H and 0 <= wj < W):
            continue
        if dist[wi][wj] != -1:
            continue
        if S[wi][wj] == "#":
            continue
        todo.append((wi, wj))
        dist[wi][wj] = dist[vi][vj] + 1

ans = 0
for i in range(H):
    for j in range(W):
        ans += dist[i][j] <= D and dist[i][j] != -1
print(ans)
