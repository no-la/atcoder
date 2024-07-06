a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

ans = True
if not(a<j and d>g):
    ans = False
elif not(b<k and e>h):
    ans = False
elif not (c<l and f>i):
    ans = False


print("Yes" if ans else "No")
