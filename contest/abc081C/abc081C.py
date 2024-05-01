N, K = map(int, input().split())
A = list(map(int, input().split()))
M = len(set(A))

from collections import defaultdict
d = defaultdict(int)

for a in A:
    d[a] += 1

ans = 0
c = 0
for v in sorted(d.values()):
    if M-c<=K:
        print(ans)
        exit()
    
    ans += v
    c += 1
