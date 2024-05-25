N, L, R = map(int, input().split())
MOD = 100

def f(n): # O(log n)
    # 2^i*j=n, 2^i*(j+1)-1<=R
    i, j = 0, n
    while j%2==0 and (2**(i+1))*(j//2 + 1)-1<=R:
        i += 1
        j //= 2
    return i, j


l = L
ans = 0
while l<=R:
    i, j = f(l)
    
    print("?", i, j)
    t = int(input())
    ans = (ans+t)%MOD

    l = (2**i)*(j+1)

print("!", ans)
