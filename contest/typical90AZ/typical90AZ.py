import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 10**9 + 7

# 因数分解
ans = 1
for l in A:
    ans *= sum(l)
    ans %= MOD

print(ans)
