H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]


def f(i, j):
    if not (0 <= i < H and 0 <= j < W):
        return

    if A[i][j] == ".":
        A[i][j] = "*"


start, goal = None, None
for i in range(H):
    for j in range(W):
        if A[i][j] == ">":
            f(i, j + 1)
        elif A[i][j] == "v":
            f(i + 1, j)
        elif A[i][j] == "<":
            f(i, j - 1)
        elif A[i][j] == "^":
            f(i - 1, j)
        elif A[i][j] == "S":
            start = (i, j)
        elif A[i][j] == "G":
            goal = (i, j)

# BFS
from collections import deque

print(*A, sep="\n")
todo = deque([start])
dist = [[-1] * W for _ in range(H)]
dist[start[0]][start[1]] = 0
while todo:
    vi, vj = todo.popleft()
    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        wi, wj = vi + di, vj + dj
        if not (0 <= wi < H and 0 <= wj < W):
            continue
        if dist[wi][wj] != -1:
            continue
        if A[wi][wj] == ".":
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj] + 1

print(dist[goal[0]][goal[1]])
