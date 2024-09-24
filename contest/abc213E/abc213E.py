from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
INF = 10**10

count = [[INF] * W for _ in range(H)]
count[0][0] = 0

for k in range(H * W):
    # DFS
    todo = deque([(i, j) for i in range(H) for j in range(W) if count[i][j] == k])

    while todo:
        vi, vj = todo.pop()
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            wi, wj = vi + di, vj + dj
            if not (0 <= wi < H and 0 <= wj < W):
                continue
            if count[wi][wj] != INF:  # 既に調べた点は飛ばす
                continue

            if S[wi][wj] == "." and count[wi][wj] > k:
                todo.append((wi, wj))
                count[wi][wj] = k

    # print(*count, "-" * 20, sep="\n")
    todo = [(i, j) for i in range(H) for j in range(W) if count[i][j] == k]
    while todo:
        vi, vj = todo.pop()
        for di in range(-2, 3):
            for dj in range(-2, 3):
                if abs(di) == abs(dj) == 2:
                    continue
                wi, wj = vi + di, vj + dj
                if not (0 <= wi < H and 0 <= wj < W):
                    continue
                if count[wi][wj] > k + 1:
                    count[wi][wj] = k + 1
    # print(*count, "-" * 20, sep="\n")
    if count[H - 1][W - 1] < INF:
        print(count[H - 1][W - 1])
        break
