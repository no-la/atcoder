import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
N = H * W

# Hは全探索
# 選んだ行がすべて同じ数字の列を見ればいい


def f(l, j):
    """P[l][j] == x なら x を返す"""
    if not l:
        return -1
    x = P[l[0]][j]
    for i in l:
        if P[i][j] != x:
            return -1
    return x


# 重複なし組み合わせ O(nCk)
import itertools

ans = 1
# bit全探索
for i in range(2**H):
    l = []
    for j in range(H):
        if not ((i >> j) & 1):
            continue
        l.append(j)
    d = [0] * (N + 1)
    # d[x]: P[t:b][j]==x なる j の個数
    for j in range(W):
        x = f(l, j)
        if x != -1:
            d[x] += 1

    ans = max(ans, len(l) * max(d))

print(ans)
