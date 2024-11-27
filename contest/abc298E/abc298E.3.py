N, A, B, P, Q = map(int, input().split())
MOD = 998244353

# MOD上で考える
# 高橋君が勝つ場合の数 / (高橋君が勝つ場合の数 + 高橋君が負ける場合の数)

t = [[0] * (N + 1) for _ in range(N + 1)]
a = [[0] * (N + 1) for _ in range(N + 1)]
# t[i][j]: 高橋くんがi回の操作ではじめてjにいる場合の数
# a[i][j]: 青木くんがi回の操作ではじめてjにいる場合の数

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
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if j != N and k != N:
                continue
            val = t[i][j] * a[i][k]
            if val == 0:
                continue
            if j == N:  # 高橋君が勝つ
                print(i, j, k, val, "=", t[i][j], "x", a[i][k])
                bunshi += val
                bunshi %= MOD
            bunbo += val
            bunbo %= MOD


ans = bunshi * pow(bunbo, -1, MOD) % MOD
print(ans)
# print(bunshi, "/", bunbo)
