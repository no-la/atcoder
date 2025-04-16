"""小課題1"""

import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = H * W
MOD = 10**9 + 7

if H > 4 or W > 4:
    print("MURI☆")
    exit()


def f(A):
    for i in range(H):
        for j in range(W):
            if not A[i][j]:
                continue
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < H and 0 <= nj < W):
                        continue
                    if A[ni][nj]:
                        return False
    return True


# bit全探索
ans = 0
N = H * W
for i in range(2**N):
    put = [[False] * W for _ in range(H)]
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        a, b = divmod(j, W)
        if C[a][b] == "#":
            break
        put[a][b] = True
    else:
        ans += f(put)

print(ans)
