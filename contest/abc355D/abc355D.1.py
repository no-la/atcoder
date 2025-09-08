N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()

from heapq import heapify, heappop, heappush

rs = []
count = 0
ans = 0

for l, r in A:
    heappush(rs, r)
    while rs and rs[0] < l:
        heappop(rs)
        count -= 1

    ans += count
    count += 1

print(ans)
