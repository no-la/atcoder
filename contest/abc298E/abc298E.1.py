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

print(*t, "-" * 20, sep="\n")
print(*a, "-" * 20, sep="\n")

takahashi = 0
fin = 0
for i in range(1, N + 1):
    # 高橋君がi回目にNに着き、青木君がi-1回でNに着いていないなら高橋君が勝つ
    fin += a[i - 1][N]
    v = t[i][N] * (pow(Q, i - 1, MOD) - fin)
    fin *= Q
    fin %= MOD
    takahashi += v
    takahashi %= MOD
    print("takahasi", i, takahashi)

aoki = 0
fin = 0
for i in range(N + 1):
    # 青木君がi回目にNに着き、高橋くんがi回でNに着いていないなら青木君が勝つ
    fin += t[i][N]
    v = a[i][N] * (pow(P, i, MOD) - fin)
    print(a[i][N], pow(P, i, MOD), fin)
    fin *= P
    fin %= MOD
    aoki += v
    aoki %= MOD
    print("aoki", i, aoki)

bunshi = takahashi
bunbo = aoki + takahashi
ans = bunshi * pow(bunbo, -1, MOD) % MOD
print(ans)
print(bunshi, "/", bunbo)
