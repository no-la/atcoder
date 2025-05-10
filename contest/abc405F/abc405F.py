import sys
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

# 直線に直して見るやつ
# 多分、クエリを昇順に尺取りっぽく見ていく感じ
# ABはスタックで、2回ずつだけ見る感じ
hq = []
for i in range(M):
    a, b = map(int, input().split())
    heappush(hq, (a, i, 0))
    heappush((b, i, 1))

Q = int(input())
queries = []
for i in range(Q):
    c, d = map(int, input().split())
    queries.append((c, d, i))

ans = [0] * Q
queries.sort()
temp = 0
count = [0] * (2 * N + 1)
for c, d, q in queries:

    while hq and c <= hq[0][0] <= d:
        a, i, x = hq[0]
