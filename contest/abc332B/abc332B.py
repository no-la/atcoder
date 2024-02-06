K, G, M = map(int,input().split())

g = 0
m = 0
for _ in range(K):
    if g==G:
        g=0
    elif m==0:
        m=M
    else:
        g+=m
        m=0
        if g>G:
            m=g-G
            g=G
print(g, m)