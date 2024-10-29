N, L, R = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**16

# x<yとしてよい
cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + A[i]

d = [(cumsum[-i - 1] + i * R, i) for i in range(N + 1)]
# d[i]: x=0, y=iとしたときの値
# print(d)
from heapq import heapify, heappop, heappush

heapify(d)

ans = cumsum[-1]
for x in range(N + 1):
    while d and N - d[0][1] < x:
        heappop(d)
    v, y = d[0]
    # print(x, y, x * L, cumsum[-y - 1] - cumsum[x], y * R)
    ans = min(ans, x * L + cumsum[-y - 1] - cumsum[x] + y * R)

print(ans)
