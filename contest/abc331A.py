M, D = map(int, input().split())
y, m, d = map(int, input().split())

ny = y
nm = m
nd = d
if d==D:
    nd = 1
    if m==M:
        nm = 1
        ny += 1
    else:
        nm += 1
else:
    nd += 1

print(ny, nm, nd)
