N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def f(k, x):
    return x & (1 << k) != 0


# 桁ごとに0になればよい
for k in range(31):
    dp = [[0, 0] * N for _ in range(N)]
    # dp[i][j][t]: (i,j)にxorがtの状態で到達できるかどうか
    dp[0][0][f(k, A[0][0])] = 1
    for i in range(N):
        for j in range(N):
            for t in range(2):
                for di, dj in [[0, 1], [1, 0]]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    dp[ni][nj][t ^ f(k, A[ni][nj])] += dp[i][j][t]
