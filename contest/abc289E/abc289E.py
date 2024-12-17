from collections import deque
from collections import defaultdict

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    d = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        d[u].append(v)
        d[v].append(u)

    # BFS

    todo = deque([(0, N - 1)])
    dist = defaultdict(lambda: -1)
    dist[(0, N - 1)] = 0
    while todo and dist[N - 1, 0] == -1:
        vt, va = todo.popleft()
        for wt in d[vt]:
            for wa in d[va]:
                if dist[wt, wa] != -1:  # 既に調べた点は飛ばす
                    continue
                if C[wt] == C[wa]:
                    continue
                if wt != N - 1 or wa != 0:
                    todo.append((wt, wa))
                dist[wt, wa] = dist[vt, va] + 1
    print(dist[N - 1, 0])
