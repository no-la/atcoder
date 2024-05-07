N, M = map(int, input().split())
d = [[None]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    
    
ans = 0
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(list(range(N)), N):
    now = l[0]
    cost = 0
    for v in l[1:]:
        if d[now][v] is None:
            break
        cost += d[now][v]
        now = v
    ans = max(ans, cost)
    
print(ans)
