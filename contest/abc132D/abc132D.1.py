N, K = map(int, input().split())
MOD = 10**9 + 7


def nHk(n, k):
    # (n+k-1)Ck
    rev = 1
    for i in range(k):
        rev *= n + k - 1 - i
        rev %= MOD
    for i in range(1, k + 1):
        rev *= pow(i, -1, MOD)
        rev %= MOD
    return rev


for i in range(1, K + 1):
    # BRBR...RBRBみたいにして、残りを適当に置く
    # iH(K-i) * (i+1)H(N-K-i+1)
    if i > N - K + 1:
        print(0)
        continue
    print(nHk(i, K - i) * nHk(i + 1, N - K - i + 1) % MOD)
