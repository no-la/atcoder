import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
S = [input() for _ in range(H)]
N = H * W

# 全ての非常口から並行してBFS
# 最後に復元する

E = [(i, j) for i in range(H) for j in range(W) if S[i][j] == "E"]

# BFS
from collections import deque

todo = deque(E)
dist = [[-1] * W for _ in range(H)]
for i, j in E:
    dist[i][j] = 0
while todo:
    vi, vj = todo.popleft()
    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        wi, wj = vi + di, vj + dj
        if wi < 0 or wi >= H or wj < 0 or wj >= W:
            continue
        if dist[wi][wj] != -1:  # 既に調べた点は飛ばす
            continue
        if S[wi][wj] == "#":
            continue
        dist[wi][wj] = dist[vi][vj] + 1
        todo.append((wi, wj))

# print(*dist, sep="\n")

ans = [["#"] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if dist[i][j] == -1:
            ans[i][j] = "#"
            continue
        if dist[i][j] == 0:
            ans[i][j] = "E"
            continue
        for di, dj, x in [[0, -1, "<"], [0, 1, ">"], [-1, 0, "^"], [1, 0, "v"]]:
            wi, wj = i + di, j + dj
            if wi < 0 or wi >= H or wj < 0 or wj >= W:
                continue
            if dist[wi][wj] == -1:
                continue
            if dist[wi][wj] == dist[i][j] - 1:
                ans[i][j] = x
                break

for i in range(H):
    print(*ans[i], sep="")
