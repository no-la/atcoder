N = int(input())
from collections import defaultdict
ans = [-1, -1]
seen = set()

for i in range(N):
    S, T = input().split()
    T = int(T)
    
    if S in seen:
        continue
    seen.add(S)
    if ans[0]<T:
        ans = [T, i+1]

print(ans[1])
