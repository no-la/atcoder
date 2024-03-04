N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]

NN = 2*N


def f(i, j):
    return A[i][j-i-1]

        

if N==1:
    print(f(0, 1))
    exit()


ans = 0
all_set = set(range(2*N))
# 全探索 N!/(N!*2^N) ~ 2*10^6
# DFS
from collections import deque
todo = deque([([0, i], f(0, i)) for i in range(1, NN)])
while todo:
    v, c = todo.pop()
    l = list(all_set-set(v))
    w1 = min(l) # O(2*N)
    for w2 in l: # O(2*N)
        if w1==w2:
            continue
        nv = v.copy() # O(2*N)
        nv.append(w1)
        nv.append(w2)
        nc = c^f(w1, w2)
        if len(nv)==NN:
            ans = max(ans, nc)
        else:
            todo.append((nv, nc))

print(ans)