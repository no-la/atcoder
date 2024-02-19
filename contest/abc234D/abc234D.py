N, K =map(int, input().split())
P = list(map(int, input().split()))


from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
q = P[:K]
heapify(q)
ans = [str(q[0])]
for i in range(K, N):
    heappush(q, P[i])
    heappop(q)
    ans.append(str(q[0]))
print("\n".join(ans))