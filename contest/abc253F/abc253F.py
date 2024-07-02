N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# まず個数の最大値を出す
A.sort()
from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
hq = []
heapify(hq)
m = 0
for l, r in A:
    while hq[0]<=l:
        heappop(hq)
    
    heappush(hq, r)
    

