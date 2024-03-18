N = int(input())
K = len(str(N))
MOD = 998244353

ans = 0
k = 1
while k<=K:
    k1 = 10**k
    k2 = 10**(k-1)
    if k1-1>N:
        ans = (ans + (N-k2+1)*(N-k2+2)//2)%MOD
    else:
        ans = (ans + (k1-k2)*(k1-k2+1)//2)%MOD
    k += 1
print(ans)