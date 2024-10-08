N, K = map(int, input().split())
MOD = 10**9 + 7

for i in range(1, K + 1):
    # KC(i-1) * (N-K-i+1)!
    ans = 1
    for j in range(i):
        ans *= K - j
        ans %= MOD
    for j in range(1, i):
        ans *= pow(j, -1, MOD)
        ans %= MOD
    for j in range(1, N - K - i + 2):
        ans *= j
        ans %= MOD
    print(ans)
