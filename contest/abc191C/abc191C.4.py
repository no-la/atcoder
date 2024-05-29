H, W = map(int, input().split())
S = [input() for _ in range(H)]

start = None
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            start = [i, j]

# DFS
from collections import deque
todo = deque([start])
seen = [[False]*W for _ in range(H)] # ここはsetでもよい
seen[start[0]][start[1]] = True

ans = 4
is_corner = [[False]*(W+1) for _ in range(H+1)]
for a in range(2):
    for b in range(2):
        is_corner[start[0]+a][start[1]+b] = True
while todo:
    vi, vj = todo.pop()
    for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
        wi, wj = vi+di, vj+dj
        if not (0<=wi<H and 0<=wj<W):
            continue
        if seen[wi][wj]: # 既に調べた点は飛ばす
            continue
        if S[wi][wj]!="#":
            continue
        
        for a in range(2):
            for b in range(2):
                if is_corner[wi+a][wj+b]:
                    is_corner[wi+a][wj+b] = False
                    ans -= 1
                elif not is_corner[wi+a][wj+b]:
                    is_corner[wi+a][wj+b] = True
                    ans += 1
        todo.append([wi, wj])
        seen[wi][wj] = True

# print(*is_corner, sep="\n")

print(ans)
