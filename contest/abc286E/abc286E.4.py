N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())
INF = 10**15

dist = [[1 if S[i][j] == "Y" else INF for j in range(N)] for i in range(N)]
# dist[i][j]: i, j間に辺があればそのコスト、なければINF
souvenir = [[0] * N for _ in range(N)]
# souvenir[i][j]: iからjに最短距離で行くときのお土産の最大値

for i in range(N):
    dist[i][i] = 0
    for j in range(N):
        souvenir[i][j] = A[i] + A[j] if i != j else A[i]

# print(*souvenir, "-" * 20, sep="\n")

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j == k:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                # kを通るルート
                dist[i][j] = dist[i][k] + dist[k][j]
                souvenir[i][j] = souvenir[i][k] + souvenir[k][j] - A[k]
            elif dist[i][j] == dist[i][k] + dist[k][j]:
                souvenir[i][j] = max(
                    souvenir[i][j], souvenir[i][k] + souvenir[k][j] - A[k]
                )
            else:
                ...

# print(*dist, "-" * 20, sep="\n")
# print(*souvenir, "-" * 20, sep="\n")
for _ in range(Q):
    u, v = map(lambda x: int(x) - 1, input().split())

    if dist[u][v] == INF:
        print("Impossible")
    else:
        print(dist[u][v], souvenir[u][v])
