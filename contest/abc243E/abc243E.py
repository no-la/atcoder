N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M): 
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((b, c))
    d[b].append((a, c))



