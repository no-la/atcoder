N = int(input())
M = 10**6


def f(a, b):
    return b**3 + a*b**2 + a**2*b + a**3

ans = 10**18
l, r = -1, M+1
for a in range(M):
    # print("a", a)
    l = -1
    while l<r-1:
    # for _ in range(10):
        # print(l, r)
        b = (l+r)//2
        v = f(a, b)
        if v<N:
            l = b
        else:
            r = b
    ans = min(ans, f(a, r))

print(ans)
