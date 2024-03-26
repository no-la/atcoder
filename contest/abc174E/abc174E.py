N, K = map(int, input().split())
A = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
B = [-a for a in A]
heapify(B)
# 大きい丸太から順に切っていく
# 切り方は、
for _ in range(K):
    a = -heappop(B)
    na = a//2 # 誤差出そ～～～～
    print(a, "->", na)
    heappush(B, -na)
    heappush(B, -na)
print(int(-B[0]))
print("------------")
print(*[-heappop(B) for _ in range(len(B))], sep="\n")