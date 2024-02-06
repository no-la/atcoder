N = int(input())
S = [input() for _ in range(N)]

N2 = N*N
N3 = N2*N
def f(p1, p2):
    return p1[0]*(N3)+p1[1]*(N2)+p2[0]*(N)+p2[1]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
p = []
for i in range(N):
    for j in range(N):
        if S[i][j]=="P":
            p.append([i, j])
#BFS
from collections import deque
todo = deque([p])
dist = [-1]*(N**4) #二人の位置関系をidにする
dist[f(p[0], p[1])] = 0
while todo:
    p1, p2 = todo.popleft()
    id = f(p1, p2)
    for i, j in delta:
        np1 = [p1[0]+i, p1[1]+j]
        np2 = [p2[0]+i, p2[1]+j]
        if not (0<=np1[0]<N and 0<=np1[1]<N) or S[np1[0]][np1[1]]=="#":
            np1 = p1.copy()
        if not (0<=np2[0]<N and 0<=np2[1]<N) or S[np2[0]][np2[1]]=="#":
            np2 = p2.copy()
        nid = f(np1, np2)
        if dist[nid]!=-1: #既に調べた点は飛ばす
            continue
        
        todo.append([np1, np2])
        dist[nid] = dist[id]+1
        if np1==np2:
            print(dist[nid])
            exit()
print(-1)