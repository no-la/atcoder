H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

d = [[[0] * (N + 1) for _ in range(W + 1)] for _ in range(H + 1)]
# d[i][j][k]: [0, i)x[0, j)にあるkの個数

for i in range(H):
    for j in range(W):
        for k in range(N + 1):
            d[i + 1][j + 1][k] = (
                d[i][j + 1][k] + d[i + 1][j][k] - d[i][j][k] + (A[i][j] == k)
            )

ans = [[0] * (W - w + 1) for _ in range(H - h + 1)]
for k in range(H - h + 1):
    for l in range(W - w + 1):
        ans[k][l] = sum(
            [
                (
                    d[H][W][v]
                    - d[k + h][l + w][v]
                    + d[k][l + w][v]
                    + d[k + h][l][v]
                    + d[k][l][v]
                )
                > 0
                for v in range(N + 1)
            ]
        )

# print(*d, sep="\n")
for l in ans:
    print(*l)
