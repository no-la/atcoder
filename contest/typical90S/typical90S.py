import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
M = 2 * N
INF = 10**10

# 区間DP
dp = [[INF if l <= r else 0 for r in range(M)] for l in range(M)]
# dp[l][r]: A[l:r+1]を消すためのコストの最小値


for k in range(1, M):
    for l in range(M):
        r = l + k
        if r >= M:
            break
        dp[l][r] = min(dp[l][r], abs(A[l] - A[r]) + dp[l + 1][r - 1])
        for c in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][c] + dp[c + 1][r])

# print(*dp, sep="\n")
print(dp[0][M - 1])
