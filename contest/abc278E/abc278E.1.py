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
for i in range(H - h + 1):
    for j in range(W - w + 1):
        ni, nj = i + h, j + w
        ans[i][j] = sum(
            [
                d[H][W][k] - (d[ni][nj][k] - d[i][nj][k] - d[ni][j][k] + d[i][j][k]) > 0
                for k in range(1, N + 1)
            ]
        )

# for i in range(H):
#     for j in range(W):
#         print(d[i + 1][j + 1][1], end=" ")
#     print("\n", end="")
for a in ans:
    print(*a)
