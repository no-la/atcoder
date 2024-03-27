from collections import deque
N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))

root = list(range(N)) # root[i]: iが属する閉路の始点
d = [None]*N # d[i]: root[i]->iのスコア
for s in range(N): # O(N)
    if root[s]:
        continue
    root[s] = s
    score = 0
    d[s][s] = score
    #DFS(一本道だけど)
    todo = deque([s])
    while todo:
        v = todo.pop()
        w = P[v]
        if root[w]: # 既に調べた点は飛ばす
            break
        root[w] = s
        d[s][w] = score
        todo.append(w)
    