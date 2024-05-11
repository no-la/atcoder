N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

s = sum(A)%MOD
d = [0]*11
for a in A:
    d[len(str(a))] += 1

ans = 0

for i in range(N-1):
    a = A[i]
    d[len(str(a))] -= 1
    s -= a
    ans = (ans + s)%MOD
    for k in range(11):
        ans = (ans + (d[k]*a%MOD)*(10**k)%MOD)%MOD

print(ans)
    
