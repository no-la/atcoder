N = int(input())
A = list(map(int, input().split()))

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
# dp[i][j][k]: 寿司が1つの皿がi個、2つの皿がj個、3つの皿がk個にするための操作回数の期待値

c1 = A.count(1)
c2 = A.count(2)
c3 = A.count(3)

dp[c1][c2][c3] = 0

for s in range(N, -1, -1):
    for i in range(min(s, c1), -1, -1):
        for j in range(min(s - i, c2), -1, -1):
            k = s - i - j
            if k > c3:
                continue
            if i == c1 and j == c2 and k == c3:
                continue
            if i + j + k + 1 == N:
                dp[i][j][k] = 1
                continue
            # p = sum([(l+1)*((N-(i+j+k+1))/N)^l] for l in range(INF))
            p = N**2 / ((N - (i + j + k + 1)) ** 2)
            q = N**2 / ((N - (i + j + k)) ** 2)
            dp[i][j][k] = (
                (dp[i + 1][j][k] + p * (i + 1) / N)
                + (dp[i - 1][j + 1][k] + q * (j + 1) / N)
                + (dp[i][j - 1][k + 1] + q * (k + 1) / N)
            )

print(*dp, sep="\n")
print(dp[0][0][0])
