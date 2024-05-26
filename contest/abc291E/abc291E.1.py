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
a = [None]*N
def f(n, s):
    """A[n]より大きい数字の個数"""
    s.add(n)
    
    temp = 0
    seen = set()
    for v in d[n]:
        if v in seen:
            continue
        temp += f(v, seen)
    
        
    a[n] = temp
    return a[n]


