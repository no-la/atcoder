N, M = map(int, input().split())
from collections import defaultdict
D = defaultdict(list)
E = []
for i in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    E[i] = (u, v, t)
    D[u].append((v, t, i))
    D[v].append((u, t, i))
Q = int(input())
INF = 10**15

dist = [[INF]*N for _ in range(N)]
# dist[i][j]: 島iから島jへの最短コスト
from collections import deque
for i in range(N):
    for j in range(i, N):
        if i==j:
            dist[i][j] = 0
            continue
        # DFS
        todo = deque([(i, j)])
        seen = [False]*N # ここはsetでもよい
        seen[todo[0]] = True
        while todo:
            vi, vj = todo.pop()
            for w in D[vi]:
                if seen[w]: # 既に調べた点は飛ばす
                    continue
                if 調べる点が満たすべき条件:
                    todo.append(点)
                    seen[w] = True


for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x)-1, input().split()))
