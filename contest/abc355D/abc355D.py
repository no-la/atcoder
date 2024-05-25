N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort()

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
R = []
heapify(R)
ans = 0
count = 0
for l, r in A:
    heappush(R, r)
    while R and R[0]<l:
        heappop(R)
        count -= 1
    ans += count
    count += 1

# print(" ")
print(ans)
