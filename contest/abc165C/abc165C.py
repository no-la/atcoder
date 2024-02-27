N, M, Q = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(Q)]
# 数列は全部で10H10=92378個
# 各数列に対して得点を求めるのはO(Q)=50
# 合わせるとO(Q*10^5)=5*10^6

# まず数列のlistをつくる
A = []
#DFS
from collections import deque
todo = deque([[i] for i in range(1, M+1)])
while todo:
    v = todo.pop()
    for w in range(v[-1], M+1):
        nv = v.copy()
        nv.append(w)
        if len(nv)==N:
            A.append(nv)
        else:
            todo.append(nv)



# 各数列に対して得点を求める
ans = 0
for l in A:
    score = 0
    for a, b, c, d in D:
        if l[b-1]-l[a-1]==c:
            score += d
    ans = max(ans, score)

print(ans)