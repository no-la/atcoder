from collections import deque

T = int(input())
INF = 10**15
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    d = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        d[a - 1].append(b - 1)
        d[b - 1].append(a - 1)

    # (takahashi, aoki)を頂点とみなしてBFS
    # BFS
    ans = -1

    todo = deque([(0, N - 1)])
    dist = [[-1] * N for _ in range(N)]
    # dist[i][j]: 頂点(i, j)に到達するまでの最短距離
    dist[0][N - 1] = 0
    while todo:
        vt, va = todo.popleft()
        for wt in d[vt]:
            for wa in d[va]:
                if dist[wt][wa] != -1:  # 既に調べた点は飛ばす
                    continue
                if C[wt] == C[wa]:
                    continue
                if (wt, wa) == (N - 1, 0):
                    ans = dist[vt][va] + 1
                    break
                todo.append((wt, wa))
                dist[wt][wa] = dist[vt][va] + 1
            else:
                continue
            break
        else:
            continue
        break
    print(ans)
