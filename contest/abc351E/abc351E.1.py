N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

O = [(0, 0), (0, 1)]
DX0 = [0]*N
DY0 = [0]*N
DX1 = [0]*N
DY1 = [0]*N
d = [None]*N

for i in range(N):
    x, y = P[i]
    k = (x+y)%2
    d[i] = k
    dx = x-O[k][0]
    dy = y-O[k][1]
    if k==0:
        DX0[i] = (dx+dy)//2
        DY0[i] = (dx-dy)//2
    else:
        DX1[i] = (dx+dy)//2
        DY1[i] = (dx-dy)//2

    # print(O[k], "->", P[i], "by", d[i])

DX0.sort()
DY0.sort()
DX1.sort()
DY1.sort()

ans = 0
for i in range(N-1):
    if d[i]==0:
        ans += (DX0[-1]-DX0[i] + DY0[-1]-DY0[i])//2
    else:
        ans += (DX1[-1]-DX1[i] + DX1[-1]-DX1[i])//2
# print(DX[-1]-DX[0] + DY[-1]-DY[0])
print(ans)
