N, K = map(int, input().split())
A = list(map(int, input().split()))

# X%Nが、N回以下でループする
dp = [-1]*(N+1) # d[i]: i回操作時のXの値
dp[0] = 0
s = [-1]*(max(A)+1) # s[A[i]]: A[i]が何回目に出て来るか
s[0] = 0
for i in range(1, N+1):
    dx = A[dp[i-1]%N]
    dp[i] = dp[i-1] + dx
    if s[dx]!=-1: # ループの終点
        start = s[dx]
        loop_size = i-start
        loop_value = dp[i] - dp[start] # (start, start+loop_size]
        break
    
    s[dx] = i


if K<=start:
    print(dp[K])
else:
    print(dp[start] + loop_value*((K-start)//loop_size) + dp[start+(K-start)%loop_size]-dp[start])
