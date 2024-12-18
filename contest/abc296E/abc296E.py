N = int(input())
A = list(map(int, input().split()))

# Kは大きいものとして考えて良さそう

# 有向グラフを考える
# x->A[x]の辺を張る
# 入次数、出次数はともに1以下である
# i=0,...,N-1に対して、iから進んだときにぶつかる閉路を考える
# その閉路に含まれる頂点jは、iから始めて辿り着くことが出来る

t_win = set()
dist = [-1] * N  # dist[i]: 各探索における、始点からの距離
for k in range(N):
    i = k
    if dist[i] != -1:
        continue
    dist[i] = 0
    route = [i]  # route[j]: j番目に通った頂点
    seen = set([i])
    while dist[A[i] - 1] == -1:
        ni = A[i] - 1
        dist[ni] = dist[i] + 1
        route.append(ni)
        i = ni
        seen.add(i)
    if A[i] - 1 in seen:
        for j in route[dist[A[i] - 1] :]:
            t_win.add(j)

print(len(t_win))
