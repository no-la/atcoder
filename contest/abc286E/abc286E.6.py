N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())
INF = 10**15

dist = [[1 if S[i][j] == "Y" else INF for j in range(N)] for i in range(N)]
# dist[i][j]: i, j間に辺があればそのコスト、なければINF
souvenir = [[A[j] if i != j else 0 for j in range(N)] for i in range(N)]
# souvenir[i][j]: dist[i][j]で採用するルートにおけるお土産の総和(A[i]は含めない)

for k in range(N):
    for i in range(N):
        for j in range(N):
            # kを通るルートを採用するか否かでsouvenirを更新する
            if dist[i][j] > dist[i][k] + dist[k][j]:  # kを通るとき
                dist[i][j] = dist[i][k] + dist[k][j]
                souvenir[i][j] = souvenir[i][k] + souvenir[k][j]
            elif (
                dist[i][j] == dist[i][k] + dist[k][j]
            ):  # kを通っても通らなくてもいいとき
                souvenir[i][j] = max(souvenir[i][j], souvenir[i][k] + souvenir[k][j])
            else:
                # そのまま
                ...


for _ in range(Q):
    u, v = map(lambda x: int(x) - 1, input().split())

    if dist[u][v] == INF:
        print("Impossible")
    else:
        print(dist[u][v], souvenir[u][v] + A[u])
