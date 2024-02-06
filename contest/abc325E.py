from heapq import heapify, heappop, heappush

N, A, B, C = map(int, input().split())
CAR = []
TRAIN = []
for i in range(N):
    l = list(map(int, input().split()))
    CAR.append([j*A for j in l])
    TRAIN.append([j*B+C for j in l])

INF = float("inf")
def dijkstra(is_car):
    start = 0 if is_car else N-1 #乗り換えが車→電車のみなので、電車のときは都市i+1から都市Nまでのコストを出す
    cost = CAR if is_car else TRAIN
    ans = [INF]*N #ans[i]:都市startから都市i+1までの(現在の)最小コスト
    ans[start] = 0
    hq = [[0, start]] #都市startから都市hq[_][1]+1までのコストhq[_][0]
    seen = [False]*N #seen[i]:都市satrtから都市i+1までの最小コストが確定したかどうか
    heapify(hq)
    while hq:
        _, curr = heappop(hq)
        seen[curr] = True #都市currは直接行ける都市の中で最小コストの都市なので、直接行くのがコスト最小
        for i in range(N):
            if seen[i]:
                continue
            to_i = ans[curr]+cost[curr][i]
            if to_i<ans[i]: #都市startから都市i+1までの最小コストが更新されるかどうか
                ans[i] = to_i
                heappush(hq, [to_i, i])
    return ans

#車のみ、電車のみでのコストを出して、どこで乗り換えるのがいいか調べる
c = dijkstra(True)
t = dijkstra(False)
ans = INF
for i in range(N):
    ans = min(ans, c[i]+t[i])
print(ans)