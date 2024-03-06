N = int(input())
MOD = 10**9 + 7
# A, C, G, Tからなる
# AGC, ACG, GACを含まない
# 長さNの文字列

dp = [0]*N # dp[i]: 長さi+1文字のときの場合の数
AG = [0]*N
AC = [0]*N
GA = [0]*N
A = [0]*N
G = [0]*N
C = [0]*N
A[0] = 1
A[1] = 4
G[0] = 1
G[1] = 4
C[0] = 1
C[1] = 4
dp[0] = 4
dp[1] = 16
AG[0] = 0
AG[1] = 1
AC[0] = 0
AC[1] = 1
GA[0] = 0
GA[1] = 1

for i in range(2, N):
    dp[i] = (dp[i-1]*4 - AG[i-1] - AC[i-1] - GA[i-1])%MOD
    AG[i] = A[i-1]
    AC[i] = A[i-1] - GA[i-1]
    GA[i] = G[i-1]
    A[i] = dp[i-1]
    G[i] = dp[i-1] - AC[i-1]
    C[i] = dp[i-1] - GA[i-1] - AG[i-1]

print(dp[-1])