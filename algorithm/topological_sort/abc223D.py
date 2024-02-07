# https://atcoder.jp/contests/abc223/submissions/50057575
N, M = map(int, input().split())
GRAPH = [[] for _ in range(N)] #GRAPH[i]:iから向かう点のリスト
for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    GRAPH[a].append(b)
    
into = [0]*N #into[i]:iに向かう点の個数
for l in GRAPH:
    for b in l:
        into[b] += 1

#DFS, BFS風
#入ってくる辺が無い点を小さい方から仕舞っていく
ans = []
from heapq import heapify, heappop, heappush
todo = [i for i in range(N) if into[i]==0][::-1]
heapify(todo)
while todo:
    v = heappop(todo)
    ans.append(v)
    for w in GRAPH[v]:
        into[w] -= 1
        if into[w]==0:
            heappush(todo, w)
if len(ans)!=N:
    print(-1)
else:
    print(" ".join(map(lambda x:str(x+1), ans)))