N, M, K = map(int, input().split())
d = [[] for _ in range(N)]
for i in range(M):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, a))
    d[v].append((u, a))
IS_SWITCH = [False] * N
for i in list(map(int, input().split())):
    IS_SWITCH[i - 1] = True

# BFS
from collections import deque

todo = deque([(0, 1)])  # (頂点, スイッチの状態)
dist = [[-1] * 2 for _ in range(N)]
# dist[i][j]: 0からiまでの距離で、iにおいてスイッチがjのものの最小値
dist[0][1] = 0
while todo:
    v, va = todo.popleft()
    for w, wa in d[v]:
        if va != wa:
            continue
        if dist[w][wa] != -1:  # 既に調べた点は飛ばす
            continue
        dist[w][wa] = dist[v][va] + 1
        todo.append((w, wa))
        # print(v, "->", w, "with", wa, f"{dist[w][wa]=}")

    if IS_SWITCH[v]:
        dist[v][va ^ 1] = dist[v][va]
        va ^= 1
        for w, wa in d[v]:
            if va != wa:
                continue
            if dist[w][wa] != -1:  # 既に調べた点は飛ばす
                continue
            dist[w][wa] = dist[v][va] + 1
            todo.append((w, wa))
            # print(v, "->", w, "with", wa, f"{dist[w][wa]=}")

# print("IS_SWITCH", IS_SWITCH)
# print(*dist, sep="\n")
if -1 in dist[N - 1]:
    print(max(dist[N - 1]))
else:
    print(min(dist[N - 1]))
