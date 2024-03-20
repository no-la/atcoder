N, Q = map(int, input().split())
M = 200000

B = [-1]*N # B[i]: 幼児iのレート
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
    b -= 1
    B[i] = a
    C[i] = b
    D[b][0].add(i)
    heappush(D[b][1], (-a, i)) # 最大値が欲しいので-aとする

E = [(-d[1][0][0], d[1][0][1]) for d in D if d[0]] # 各園の最大レートの園児のレートと、園児のid
F = set([e[1] for e in E]) # 各園の最大レートの園児一覧
heapify(E)

for _ in range(Q):
    c, d = map(lambda x: int(x)-1, input().split())
    # 元の幼稚園の情報を更新
    D[C[c]][0].remove(c)
    while D[C[c]][1] and D[C[c]][1][0][1] not in D[C[c]][0]:
        heappop(D[C[c]][1])
    # 全体の情報を更新
    if c in F:
        F.remove(c)
        if D[C[c]][1]:
            F.add(D[C[c]][1][0][1])
            heappush(E, (-D[C[c]][1][0][0], D[C[c]][1][0][1]))
    
    before = D[d][1][0] if D[d][1] else -1 # 移動前の幼稚園dの最大レートの幼児
    C[c] = d
    # 移動後の幼稚園の情報を更新
    D[d][0].add(c)
    heappush(D[d][1], (-B[c], c))
    # 全体の情報を更新
    if D[d][1][0]!=before: # 移動後の幼稚園の最大レートが変わったとき
        if before != -1:
            F.remove(before[1])
        F.add(c)
        heappush(E, (B[c], c))
    while E[0][1] not in F:
        heappop(E)
        
    # print(C)
    # print(F)
    # print(E)
    print(E[0][0])
