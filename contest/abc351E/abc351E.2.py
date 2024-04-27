N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

O = [(0, 0), (0, 1)]
DX = [0]*N
DY = [0]*N
d = [None]*N

for i in range(N):
    x, y = P[i]
    k = (x+y)%2
    d[i] = k
    dx = x-O[k][0]
    dy = y-O[k][1]
    DX[i] = (dx+dy)//2
    DY[i] = (dx-dy)//2

    # print(O[k], "->", P[i], "by", d[i])

for i in range(N-1):
    for j in range(i+1, N):
        print(P[i], "->", P[j], "by", (DX[j]-DX[i], DY[j]-DY[i]) if d[i]==d[j] else 0)
# print(ans)
