N = int(input())
A = list(map(int, input().split()))

# 桁ごとに累積和
# 30桁見れば十分
M = 30

ans = 0
for i in range(M):
    d = [0]*(N+1)
    for j in range(1, N+1):
        d[j] = (d[j-1] + (A[j-1] & (1<<i) != 0))%2
    
    c0 = d.count(0) - (d[0]==0)
    c1 = N - c0
    
    ans += c0*c1
    print(1<<i, d)


print(ans)

