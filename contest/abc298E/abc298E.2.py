N, A, B, P, Q = map(int, input().split())
MOD = 998244353

# MOD上で考える
# 高橋君が勝つ場合の数 / (高橋君が勝つ場合の数 + 高橋君が負ける場合の数)

t = [[0] * (N + 1) for _ in range(N + 1)]
a = [[0] * (N + 1) for _ in range(N + 1)]
# t[i][j]: 高橋くんがi回の操作でjにいる場合の数
# a[i][j]: 青木くんがi回の操作でjにいる場合の数

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

print(*t, "-" * 20, sep="\n")
print(*a, "-" * 20, sep="\n")

win = 0
lose = 0
for i in range(1, N + 1):
    # 高橋君がi回目にNに着き、青木君がi-1回でNに着いていないなら高橋君が勝つ
    win += t[i][N] * sum(a[i - 1][:N])
    # 高橋君がi回目にNについておらず、青木君がi回目でNについていれば高橋君が負ける
    lose += sum(t[i][:N]) * a[i][N]
    win %= MOD
    lose %= MOD


bunshi = win
bunbo = win + lose
ans = bunshi * pow(bunbo, -1, MOD) % MOD
print(ans)
print(bunshi, "/", bunbo)
