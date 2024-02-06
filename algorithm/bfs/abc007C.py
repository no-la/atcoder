#https://atcoder.jp/contests/abc007/submissions/49589406
H, W = map(int, input().split())
S = list(map(lambda x:int(x)-1, input().split()))
G = list(map(lambda x:int(x)-1, input().split()))
A = [list(input()) for _ in range(H)]
        
#BFS
from collections import deque
todo = deque([S])
seen = [-1]*(H*W)
seen[S[1]*H+S[0]] = 0
while todo:
    v = todo.popleft()
    for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = v[0]+di, v[1]+dj
        if not (0<=ni<H and 0<=nj<W):
            continue
        id = nj*H + ni
        if seen[id]!=-1:
            continue
        if A[ni][nj]==".":
            todo.append((ni, nj))
            seen[id] = seen[v[1]*H+v[0]]+1
print(seen[G[1]*H+G[0]])