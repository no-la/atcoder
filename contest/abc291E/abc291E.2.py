N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
to_count = [0]*N
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    d[x].append(y)
    to_count[y] += 1

# root
root = None
for i in range(N):
    if to_count[i]==0:
        if root is not None:
            print("No")
            exit()
        
        root = i

# print(root, to_count)

import sys
sys.setrecursionlimit(10**6)
A = [-1]*N
def f(v, c):
    if c<=A[v]:
        return
    A[v] = c
    
    if c==N:
        print("Yes")
        print(*A)
        exit()
    
    d[v].sort(key=lambda x: A[x])
    for w in d[v]:
        f(w, c+1)

f(root, 1)
print("No")
    