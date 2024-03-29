N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

# 累積和
d = [0]*N
d[0] = A[0]
for i in range(1, N):
    d[i] = (d[i-1] + A[i])%MOD

ans = 0
for i in range(N):
    ans = (ans + (A[i]*(d[-1]-d[i])%MOD)%MOD)%MOD
print(ans)