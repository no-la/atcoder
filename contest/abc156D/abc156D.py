n, a, b = map(int, input().split())

MOD = (10**9) + 7

import math

MAX_OP = n # 操作の最大回数
DB_NUM = int(math.log2(MAX_OP)) + 1

# dp[i]: 2^(2^i)
dp = [0 for _ in range(DB_NUM)]

# dp[0]を初期化
dp[0] = 2

for k in range(1, DB_NUM):
        dp[k] = (dp[k-1]**2) % MOD


# n回操作後の頂点を得る
m = 1
for i in range(DB_NUM):
    if n>>i & 1:
        m = (m*dp[i]) % MOD
m -= 1

def c(s, t):
    # sCt
    if s-t<t:
        t = s-t
    u = 1
    for i in range(t):
        u = (u*(s-i)) % MOD
    v = 1
    for i in range(t):
        v = (v*(i+1)) % MOD
    # v'*(sCt) = u', v'~v, u~u' mod MOD -> sCt~?
    # sCt~u*(v^-1)
    # mod MODにおけるvの逆元を求めればよい
    return u*pow(v, -1, MOD) % MOD

ma = c(n, a)
mb = c(n, b)
print((m - ma - mb)%MOD)