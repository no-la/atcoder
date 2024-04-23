import math
T = int(input())

def extended_gcd(x, y):
    if x == 0:
        return (y, 0, 1)
    else:
        gcd, a, b = extended_gcd(y % x, x)
        return (gcd, b - (y // x) * a, a)
for _ in range(T):
    N, S, K = map(int, input().split())
    g, a, b= extended_gcd(N, K)
    print(f"{a}*{N}+{b}*{K}={g}")
    if S%g==0:
        print((S//g)*a)
    else:
        print(-1)
    
