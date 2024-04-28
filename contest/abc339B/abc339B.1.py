H, W, N = map(int, input().split())

d = [[0]*W for _ in range(H)]
di, dj = -1, 0

def rotate(i, j, to_right):
    rvs = [[0, -1],[-1, 0],[0, 1],[1, 0]]
    for k in range(4):
        if [i, j]==rvs[k]:
            return rvs[(k+(1 if to_right else -1))%4]

i, j = 0, 0
for _ in range(N):
    d[i][j] = (d[i][j]+1)%2
    di, dj = rotate(di, dj, d[i][j]==1)
    i = (i+di)%H
    j = (j+dj)%W

for i in range(H):
    print(*["." if s==0 else "#" for s in d[i]], sep="")

