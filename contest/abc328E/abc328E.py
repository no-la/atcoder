from heapq import heapify, heappop, heappush

N, M, K = map(int, input().split())
G = {}
for i in range(M):
    u, v, w = map(int, input().split())
    if u not in G:
        G[u] = []
    if v not in G:
        G[v] = []
    G[u].append([w, v])
    G[v].append([w, u])
    

INF = float("inf")
def dijkstra(start):
    ans = [INF]*N #ans[i]:都市startから都市i+1までの(現在の)最小コスト
    ans[start] = 0
    hq = [(0, start)] #startからhq[_][1]+1までの重みhq[_][0]
    seen = [False]*N #seen[i]:satrtからi+1までの最小コストが確定したかどうか
    heapify(hq)
    while hq:
        _, curr = heappop(hq)
        seen[curr] = True #currは直接行ける都市の中で最小コストなので、直接行くのがコスト最小
        for l in G[curr]: #currから行ける点の重み, 点
            if seen[l[1]]:
                continue
            to_l = ans[curr]+l[0]
            if to_l<ans[i]: #startからi+1までの最小コストが更新されるかどうか
                ans[i] = to_l
                heappush(hq, (to_l, i))
    return ans

ans = []
for i in range(N):
    ans.append(dijkstra(i)%K)

print(min(ans))