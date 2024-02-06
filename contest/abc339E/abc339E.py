N, D = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A)

dp = [0]*500001 #dp[i]:最後の数字がiである最大の部分列の長さ

for i in range(N):
    m = 0
    #区間内の最大のdp[i]を見つければいいので、2分探索でいける？
    for d in B:
        if d-A[i]>D:
            break
        if abs(A[i]-d)>D:
            continue
        m = max(m, dp[d])
    dp[A[i]] = max(dp[A[i]-1], m+1)

print(max(dp))