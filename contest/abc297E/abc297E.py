N, K = map(int, input().split())
A = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)

hq = list(set(A))
seen = set(hq)
heapify(hq)
count = 0
while count+1<K:
    v = heappop(hq)
    count += 1
    for a in A:
        if v+a not in seen:
            heappush(hq, v+a)
            seen.add(v+a)

print(hq[0])
