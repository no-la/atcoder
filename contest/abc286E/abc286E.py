N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())

from collections import deque
for _ in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    # u->v
    # まず最短距離をだす
    # BFS
    todo = deque([s])
    dist = [-1]*N #todo[0]からの距離のリスト
    dist[todo[0]] = 0
    while todo:
        v = todo.popleft()
        for w in range(N):
            if S[v][w]=="N":
                continue
            if dist[w]!=-1: # 既に調べた点は飛ばす
                continue
            todo.append(w)
            dist[w] = dist[v]+1
            if w==t:
                break
    if dist[t]==-1:
        print("Impossible")
        continue
    size = dist[t]
    print(s, t, size)
     
            
            
            