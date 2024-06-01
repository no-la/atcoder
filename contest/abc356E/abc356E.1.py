N = int(input())
A = list(map(int, input().split()))
A.sort()

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
ans = 0
q = [(0, 1, 0)]
heapify(q)
for i in range(1, N-1):
    if A[i]>=A[q[0][0]]*q[0][1]:
        j, d, l = heappop(q)
        ans += d*(i-l)
        heappush(q, (j, d+1, i))
    heappush(q, (i, 1, i))
print(ans)
