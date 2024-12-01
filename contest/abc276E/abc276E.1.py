from collections import deque

H, W = map(int, input().split())
C = [input() for _ in range(H)]

S = []
for i in range(H):
    for j in range(W):
        if C[i][j] == "S":
            S = (i, j)
            break
    if S:
        break

achieve = [[[0] * W for _ in range(H)] for _ in range(4)]
k = 0
for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
    t = (S[0] + di, S[1] + dj)
    if not (0 <= t[0] < H and 0 <= t[1] < W):
        continue
    if C[t[0]][t[1]] != ".":
        continue
    # DFS
    todo = deque([t])
    seen = set([S, t])
    achieve[k][t[0]][t[1]] = 1
    while todo:
        vi, vj = todo.pop()
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            wi, wj = vi + di, vj + dj
            if not (0 <= wi < H and 0 <= wj < W):
                continue
            if (wi, wj) in seen:
                continue
            if C[wi][wj] == ".":
                todo.append((wi, wj))
                seen.add((wi, wj))
                achieve[k][wi][wj] = 1
    k += 1

# for k in range(4):
#     print(*achieve[k], "-" * 20, sep="\n")

for i in range(H):
    for j in range(W):
        count = 0
        for k in range(4):
            count += achieve[k][i][j]
        if count >= 2:
            print("Yes")
            exit()

print("No")
