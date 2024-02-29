N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))


# N回以下の操作でループするはずなので、その数を求めればいい
now = 0
D = [-1]*(N+1) # D[i]: i番目に来る町
dist = [-1]*N
dist[now] = 0
D[0] = now
while True:
    ne = A[now]
    if dist[ne]!=-1:
        start = dist[ne]
        loop = dist[now]+1-dist[ne]
        break
    dist[ne] = dist[now]+1
    D[dist[ne]] = ne
    if dist[ne]==K:
        print(ne+1)
        exit()
    now = ne
print(D[(K-start)%loop+start]+1)