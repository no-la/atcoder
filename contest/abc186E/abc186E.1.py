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
    g, a, b = extended_gcd(-K, N)
    # print(f"f {a}x{K}+{b}x{N}={g}")
    if S%g==0:
        # print(f"{(S//g)*a}*{N}+{(S//g)*b}*{K}={0}")
        # print((((S)//g)*b)%N)
        x0 = ((S)//g)*a
        y0 = ((S)//g)*b
        # print(f"s {x0}x{K}+{y0}x{N}={S}")
        xdelta = N//g
        ydelta = K//g
        x = x0 - xdelta*(x0//xdelta)
        y = y0 - ydelta*(x0//xdelta)
        # print(f"t {x}x{K}+{y}x{N}={S}")
        print(x0 - xdelta * -(-x0//xdelta))
    else:
        print(-1)
    
