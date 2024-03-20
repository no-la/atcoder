N, Q = map(int, input().split())
M = 200000

C = [-1]*N # C[i]: 幼児iが所属している園

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
D = [[set(), []] for _ in range(M)] # D[i]: 在籍している幼児の一覧, レートのheapq
for i in range(M):
    heapify(D[i][1])

for i in range(N):
    a, b = map(int, input().split())
    C[i] = b
    b -= 1
    D[b][0].add(i)
    heappush(D[b][1], (-a, i)) # 最大値が欲しいので-aとする

E = [-d[1][0] for d in D] # 各園の最大レートの園児のレートと、園児のid
F = set([e[1] for e in E]) # 各園の最大レートの園児一覧
heapify(E)

for _ in range(Q):
    c, d = map(lambda x: int(x)-1, input().split())
    if D[C[c]][1][0][0] == c: # 元の幼稚園の最大レートが幼児cのとき
        ...
    C[c] = d
    if D[C[c]][1][0][0] < c: # 移動後の幼稚園の最大レートが幼児cのとき
        ...
