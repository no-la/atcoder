N = int(input())
A = [[] for _ in range(N-1)] #A[i][_]: ステージiから、ステージ[1]に行くのにかかる時間[0]

for i in range(N-1):
    a, b, x = map(int, input().split())
    A[i].append((a, i+1))
    A[i].append((b, x-1))


INF = 1000000000000000000
from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)

#BFS
todo = [(l[0], l[1], 0) for l in A[0]]
heapify(todo)
ans = [INF]*N
ans[0] = 0
count = 0
while todo:
    cost, to, from_ = heappop(todo)
    if from_==to:
        continue
    ans[to] = min(ans[to], cost)
    if to==N-1:
        break
    for ncost, nto in A[to]:
        if ans[nto] < INF: #既に調べた点は飛ばす
            continue
        heappush(todo, (cost+ncost, nto, to))

print(ans[N-1])