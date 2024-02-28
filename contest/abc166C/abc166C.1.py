N, M = map(int, input().split())
H = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)


ans = 0
for i in range(N):
    for j in d[i]:
        if H[i]<=H[j]:
            break
    else:
        ans += 1
print(ans)