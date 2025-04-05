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
            # 前蹴り
            count[wi][wj] = count[vi][vj] + 1
            ui, uj = wi + di, wj + dj
            todo.append((wi, wj))
            if 0 <= ui < H and 0 <= uj < W:
                count[ui][uj] = min(count[ui][uj], count[wi][wj])
                todo.append((ui, uj))
        else:
            count[wi][wj] = min(count[wi][wj], count[vi][vj])
            todo.append((wi, wj))

print(*count, sep="\n")
print(count[C][D])
