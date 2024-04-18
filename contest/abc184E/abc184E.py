H, W = map(int, input().split())
A = [input() for _ in range(H)]

from collections import defaultdict
d = defaultdict(list)

for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            start = (i, j)
        elif A[i][j]=="G":
            goal = (i, j)
        elif A[i][j].isalpha():
            d[A[i][j]].append((i, j))


# BFS
from collections import deque
todo = deque([start])
dist = [[-1]*W for _ in range(H)] #todo[0]からの距離のリスト
dist[start[0]][start[1]] = 0
while todo:
    vi, vj = todo.popleft()
    while d[A[vi][vj]]:
        wi, wj = d[A[vi][vj]].pop()
        if not (0<=wi<H and 0<=wj<W):
            continue
        if dist[wi][wj]!=-1: # 既に調べた点は飛ばす
            continue
        
        ndist = dist[vi][vj]+1
        if A[wi][wj]=="G":
            print(ndist)
            exit()
        if A[wi][wj]!="#":
            todo.append((wi, wj))
            dist[wi][wj] = ndist
    for wi, wj in [[vi, vj-1],[vi, vj+1],[vi-1, vj],[vi+1, vj]]:
        if not (0<=wi<H and 0<=wj<W):
            continue
        if dist[wi][wj]!=-1: # 既に調べた点は飛ばす
            continue
        
        ndist = dist[vi][vj]+1
        if A[wi][wj]=="G":
            print(ndist)
            exit()
        if A[wi][wj]!="#":
            todo.append((wi, wj))
            dist[wi][wj] = ndist
print(-1)
