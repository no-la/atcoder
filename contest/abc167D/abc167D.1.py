N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))


# N回以下の操作でループするはずなので、その数を求めればいい
D = [-1]*(N+1) # D[i]: i番目に来る町
dist = [-1]*N
D[0] = 0
dist[0] = 0
for i in range(1, N+1):
    ne = A[D[i-1]]
    if dist[ne]!=-1:
        start = dist[ne]
        loop = i-dist[ne]
        break
    if i==K:
        print(ne+1)
        exit()
    D[i] = ne
    dist[ne] = i
print(D[(K-start)%loop + start] + 1)