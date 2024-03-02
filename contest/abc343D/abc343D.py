N, T = map(int, input().split())
from collections import defaultdict
d = defaultdict(int) # d[i]: iが出て来る回数
A = [0]*N # A[i]: 選手iの今の得点
d[0] = N
kinds = 1
for _ in range(T):
    a, b = map(int, input().split())
    a -= 1
    before = A[a]
    A[a] += b
    
    d[before] -= 1
    if d[before]==0:
        kinds -=1
    
    if d[A[a]]==0:
        kinds += 1
    d[A[a]] += 1
    print(kinds)