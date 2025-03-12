import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
MOD = 10**9 + 7

if N == 1:
    print(K)
else:
    # K * K-1 * K-2 * K-2 * ...
    print((K * (K - 1)) % MOD * pow(K - 2, N - 2, MOD) % MOD)
