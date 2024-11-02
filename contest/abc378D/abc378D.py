H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

from functools import cache


# メモ化再帰
# @cache
def f(seen, i, j):
    if len(seen) == K + 1:
        return 1
    elif len(seen) > K + 1:
        return 0
    temp = 0
    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if S[ni][nj] == "#":
            continue
        if (ni, nj) in seen:
            continue
        temp += f(seen | set((ni, nj)), ni, nj)
    return temp


print(sum([f(set((i, j)), i, j) for i in range(H) for j in range(W) if S[i][j] == "#"]))
