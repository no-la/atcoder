N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 調べる必要のある移動は岩の個数x12程度なので、全探索でよい
ans = [[False]*M for _ in range(N)]
ans[1][1] = True

left = [[None]*M for _ in range(N)]
right = [[None]*M for _ in range(N)]
up = [[None]*M for _ in range(N)]
down = [[None]*M for _ in range(N)]
for i in range(N):
    l, r = 1, 1
    while r<M:
        if S[i][l]=="#":
            l += 1
            r = l
            continue
        while r<M and S[i][r]==".":
            r += 1
        left[i][r-1] = l
        right[i][l] = r-1
        print(i, l, r)
        l = r+1
        r = l

for j in range(M):
    u, d = 1, 1
    while d<N:
        if S[u][j]=="#":
            u += 1
            d = u
            continue
        while d<N and S[d][j]==".":
            d += 1
        up[d-1][j] = u
        down[u][j] = d-1
        u = d+1
        d = u
        
# print(*left, "-"*20, sep="\n")
# print(*right, "-"*20, sep="\n")

# DFS
from collections import deque
todo = deque([(1, 1)])
seen = [[False]*M for _ in range(N)] # ここはsetでもよい
seen[todo[0]] = True
while todo:
    vi, vj = todo.pop()
    for wj in [right[vi][vj], left[vi][vj]]:
        if wj is None:
            continue
        wi = vi
        if seen[wi][wj]:
            continue
        todo.append((wi, wj))


