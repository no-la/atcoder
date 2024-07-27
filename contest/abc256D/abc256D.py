N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = 200000

A.sort()

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
hq = []
heapify(hq)
# hq: 右の人たち


ans = []
j = 0
l = 1
for i in range(1, M+1):
    while j<N and A[j][0]==i:
        heappush(hq, A[j][1])
        j += 1

    while hq and hq[0]==i:
        heappop(hq)
        
    if not hq:
        if l<i:
            ans.append([l, i])
        l = i+1


for l in ans:
    print(*l)
