H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]


start, goal = None, None

# start, goal
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start = (i, j)
            A[i][j] = "."
        elif A[i][j] == "G":
            goal = (i, j)
            A[i][j] = "."

# right
for i in range(H):
    j = 0
    while j < W:
        if A[i][j] != ">":
            j += 1
            continue

        j += 1
        while j < W and A[i][j] == ".":
            A[i][j] = "*"
            j += 1
# left
for i in range(H):
    j = W - 1
    while j >= 0:
        if A[i][j] != "<":
            j -= 1
            continue

        j -= 1
        while j >= 0 and A[i][j] in [".", "*"]:
            A[i][j] = "*"
            j -= 1
# up
for j in range(W):
    i = H - 1
    while i >= 0:
        if A[i][j] != "^":
            i -= 1
            continue

        i -= 1
        while i >= 0 and A[i][j] in [".", "*"]:
            A[i][j] = "*"
            i -= 1
# down
for j in range(W):
    i = 0
    while i < H:
        if A[i][j] != "v":
            i += 1
            continue

        i += 1
        while i < H and A[i][j] in [".", "*"]:
            A[i][j] = "*"
            i += 1

# BFS
from collections import deque

# print(*A, sep="\n")
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
