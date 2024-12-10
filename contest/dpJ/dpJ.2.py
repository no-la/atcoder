N = int(input())
A = list(map(int, input().split()))

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
# dp[i][j][k]: 寿司が1つの皿がi個、2つの皿がj個、3つの皿がk個の状態から寿司を全て無くすための操作回数の期待値
dp[0][0][0] = 0

c1 = A.count(1)
c2 = A.count(2)
c3 = A.count(3)
# 求める答えは dp[c1][c2][c3]

sa = sum(A)

for s in range(1, sa + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            k = s - i * 1 - j * 2
            if k % 3 != 0 or k < 0 or k > 3 * N:
                continue
            k //= 3
            if i + j * 2 + k * 3 != s:
                continue
            # dp[i][j][k] = dp[i][j][k]*(N-i-j-k)/N
            # + dp[i+1][j][k]*(i+1)/N
            # + dp[i-1][j+1][k]*(j+1)/N
            # + dp[i][j-1][k+1]*(k+1)/N
            # + 1
            dp[i][j][k] = (
                (
                    (dp[i - 1][j][k] * i / N if i > 0 else 0)
                    + (dp[i + 1][j - 1][k] * j / N if i < N and j > 0 else 0)
                    + (dp[i][j + 1][k - 1] * k / N if j < N and k > 0 else 0)
                    + 1
                )
                * N
                / (i + j + k)
            )

print(dp[c1][c2][c3])
