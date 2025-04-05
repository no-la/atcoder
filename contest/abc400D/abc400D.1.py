import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
S = [input() for _ in range(H)]
A, B, C, D = map(lambda x: int(x) - 1, input().split())
N = H * W
INF = 10**18

count = [[INF] * W for _ in range(H)]
# count[i][j]: (i, j) に行くための前蹴りの最小回数
count[A][B] = 0

# 嘘DFS
from collections import deque

todo = deque([(A, B)])
target = []
while count[C][D] == INF and todo:
    while todo:
        vi, vj = todo.pop()
        target.append((vi, vj))
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            wi, wj = vi + di, vj + dj
            if not (0 <= wi < H and 0 <= wj < W):
                continue
            if count[wi][wj] <= count[vi][vj]:
                continue
            if S[wi][wj] == "#":
                continue
            count[wi][wj] = count[vi][vj]
            todo.append((wi, wj))
    # 前蹴り
    while target:
        vi, vj = target.pop()
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            wi, wj = vi + di, vj + dj
            if not (0 <= wi < H and 0 <= wj < W):
                continue
            if S[wi][wj] != "#":
                continue

            for x in [1, 2]:
                wi, wj = vi + x * di, vj + x * dj
                if not (0 <= wi < H and 0 <= wj < W):
                    continue
                if count[wi][wj] <= count[vi][vj] + 1:
                    continue
                count[wi][wj] = count[vi][vj] + 1
                todo.append((wi, wj))

    # print(*count, sep="\n")
print(count[C][D])
