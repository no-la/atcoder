import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
MOD = 10**9

A = [1] * (N + 1)
cumsum = [0] * (N + 2)
for i in range(N + 1):
    if i < K:
        A[i] = 1
    else:
        A[i] = cumsum[i] - cumsum[i - K]

    cumsum[i + 1] = cumsum[i] + A[i]
    cumsum[i + 1] %= MOD

print(A[N] % MOD)
