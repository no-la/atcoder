N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 全探索

# まず、全パターン列挙する O(N*2^N)
P = []
#DFS
from collections import deque
todo = deque([[i] for i in range(M)])
while todo:
    v = todo.pop()
    for w in range(v[-1]+1, N):
        nv = v.copy()
        nv.append(w)
        if w==N-1:
            P.append(nv)
        else:
            todo.append(nv)

ans = 10000000000
for l in P:
    a = [0]*M
    for i in l:
        for j in range(1, M+1):
            a[j-1] += A[i][j]
    if all([k>=X for k in a]):
        ans = min(ans, sum([A[i][0] for i in l]))
print(ans if ans!=10000000000 else -1)