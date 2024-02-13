# https://atcoder.jp/contests/abc222/submissions/50243918
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab_max = max(max(A), max(B))+1
mod = 998244353

ans = 0
dp = [[0]*ab_max for _ in range(N)] # dp[i][j]:0~iまでで、i番目がj以下の数列の個数

# 初期値
for i in range(ab_max):
    right = min(i, B[0])
    dp[0][i] = right-A[0]+1 if A[0]<=right else 0

for i in range(1, N):
    dp[i][0] = dp[i-1][0] if A[i]==0 else 0
    for j in range(1, ab_max):
        if j<A[i]:
            dp[i][j] = 0
        elif A[i]<=j<=B[i]:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%mod
        else:
            dp[i][j] = dp[i][B[i]]
            
print(dp[-1][-1]%mod)