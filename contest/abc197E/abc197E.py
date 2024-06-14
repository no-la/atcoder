N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N):
    x, c = map(int, input().split())
    d[c].append(x)

for k in d:
    d[k].sort()

d = sorted(d.items())
d.append((10**9+1, [0]))
# print(*d)

now = 0
ans = 0
for i in range(len(d)):
    x = d[i][1]
    if now<=x[0]:
        # print(now, "->", x[-1])
        ans += abs(x[-1]-now)
        now = x[-1]
        continue
    if x[-1]<=now:
        # print(now, "->", x[0])
        ans += abs(now-x[0])
        now = x[0]
        continue
    
    # x[0] < now < x[-1]
    nx = d[i+1][1]
    if now<=nx[-1]:
        # print(now, "->", x[0], "->", x[-1])
        ans += abs(now-x[0])
        ans += abs(x[-1]-x[0])
        now = x[-1]
    else:
        # print(now, "->", x[-1], "->", x[0])
        ans += abs(x[-1]-now)
        ans += abs(x[-1]-x[0])
        now = x[0]
        
print(ans)
