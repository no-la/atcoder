from collections import deque

N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

E = [[j for j in range(N) if S[i][j] == "Y"] for i in range(N)]

Q = int(input())
INF = 10**15

for _ in range(Q):
    U, V = map(lambda x: int(x) - 1, input().split())

    # BFS
    todo = deque([U])
    dist = [INF] * N  # todo[0]からの距離のリスト
    dist[U] = 0
    souvenir = [0] * N
    souvenir[U] = A[U]
    while todo:
        v = todo.popleft()
        ndist = dist[v] + 1
        for w in E[v]:
            if dist[w] < ndist:
                continue
            else:
                souvenir[w] = max(souvenir[w], souvenir[v] + A[w])
                if dist[w] == INF:
                    todo.append(w)
                    dist[w] = ndist

    # print(dist, sep="\n")
    if dist[V] == INF:
        print("Impossible")
    else:
        print(dist[V], souvenir[V])
