import sys

input = lambda: sys.stdin.readline().rstrip()
A, O, B, G = map(int, input().split())
S = A + O + B + G
MOD = 998244353

N = S


# 前計算
fact = [1] * (N + 1)
fact_inv = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i
    fact_inv[i] = fact_inv[i - 1] * pow(i, -1, MOD)
    fact[i] %= MOD
    fact_inv[i] %= MOD


def comb(n, r):
    """n!/r!(n-r)!"""
    return fact[n] * fact_inv[r] * fact_inv[n - r] % MOD


ans = 0

for i in range(G, G + B + 1):
    # 一番左のブドウが、右から数えてi番目にあるとき

    # まずバナナの配置
    # temp = math.comb(i - 1, i - G) % MOD
    temp = comb(i - 1, i - G) % MOD

    # リンゴを置いて、オレンジを置く
    # temp *= math.comb(S - i, O) % MOD
    temp *= comb(S - i, O) % MOD

    ans += temp
    ans %= MOD

print(ans)
