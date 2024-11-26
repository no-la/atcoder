N, A, B, P, Q = map(int, input().split())
MOD = 998244353

# MOD上で考える

t = [[0] * (N + 1) for _ in range(N + 1)]
a = [[0] * (N + 1) for _ in range(N + 1)]
# t[i][j]: 高橋くんがi回の操作でj以上にいる場合の数
# a[i][j]: 青木くんがi回の操作でj以上にいる場合の数

for dp, S, M in [[t, A, P], [a, B, Q]]:
    dp[0][S] = 1
    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0:
                continue
            ni = i + 1
            for x in range(1, M + 1):
                nj = min(j + x, N)
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= MOD

# print(*t, "-" * 20, sep="\n")
# print(*a, "-" * 20, sep="\n")

bunshi = 0
bunbo = 0
for i in range(N + 1):
    # 高橋君がi回目にNに着き、青木君がi-1回でNに着いていないなら高橋君が勝つ
    bunshi += t[i][N] * (pow(Q, i - 1, MOD) - a[i - 1][N])
    bunbo += pow(P, i, MOD) * pow(Q, i - 1, MOD)

    bunshi %= MOD
    bunbo %= MOD

ans = bunshi * pow(bunbo, -1, MOD) % MOD
print(ans)
print(bunshi, "/", bunbo)
