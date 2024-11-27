N, A, B, P, Q = map(int, input().split())
MOD = 998244353

dp = [[[0] * 2 for _ in range(N + 1)] for _ in range(N + 1)]
# dp[i][j][f]: 高橋君がi、青木君がjにいて、次の手番がf(0なら高橋君)のときの高橋君の勝率

# init
for i in range(1, N + 1):
    for f in range(2):
        dp[N][i][f] = 1
        dp[i][N][f] = 0
dp[N][N][0] = 0  # この二つは見ない
dp[N][N][1] = 0

for i in range(N - 1, A - 1, -1):
    for j in range(N - 1, B - 1, -1):
        f = 0
        for k in range(1, P + 1):
            dp[i][j][f] += dp[min(N, i + k)][j][f ^ 1]
            dp[i][j][f] %= MOD
        dp[i][j][f] *= pow(P, -1, MOD)
        dp[i][j][f] %= MOD
        f = 1
        for k in range(1, Q + 1):
            dp[i][j][f] += dp[i][min(N, j + k)][f ^ 1]
            dp[i][j][f] %= MOD
        dp[i][j][f] *= pow(Q, -1, MOD)
        dp[i][j][f] %= MOD

# print(*dp, sep="\n")
print(dp[A][B][0])
