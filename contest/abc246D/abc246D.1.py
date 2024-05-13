N = int(input())
M = 10**6


def f(a, b):
    return b**3 + a*b**2 + a**2*b + a**3

ans = 10**18
b = M
for a in range(M):
    # print("a", a)
    while True:
        # print(l, r)
        v = f(a, b)
        if v<N:
            ans = min(ans, f(a, b+1))
            break
        elif b==0:
            ans = min(ans, v)
            break
        else:
            b -= 1
    

print(ans)
