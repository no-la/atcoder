N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

D = [[[] for __ in range(10)] for _ in range(10)] # D[i][j]: D[i][j]*j%10 == i
for i in range(10):
    for j in range(10):
        D[(i*j)%10][j].append(i)

dp = [[0]*10 for _ in range(N)] # dp[i][j]: A[:i+1]でjを作る場合の数 % MOD
dp[0][A[0]] = 1
for i in range(1, N):
    for j in range(10):
        # F
        dp[i][j] = dp[i-1][(j-A[i])%10] % MOD
        # G
        for k in D[j][A[i]]:
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

print("\n".join(map(str, dp[-1])))