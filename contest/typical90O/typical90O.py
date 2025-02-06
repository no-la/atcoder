import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
MOD = 10**9 + 7

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


ans = [0] * (N + 1)
for k in range(1, N + 1):
    for i in range(1, N + 1):
        # i個選ぶとき
        n, r = N - (k - 1) * (i - 1), i
        if n < r:
            break
        ans[k] += comb(n, r)
        ans[k] %= MOD
print(*ans[1:], sep="\n")
