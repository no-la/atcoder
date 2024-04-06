N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N):
    a, c = map(int, input().split())
    d[c].append(a)

ans = (0, -1) # 美味しさの最小値, 色
for c in d:
    d[c].sort()
    ans = max(ans, (d[c][0], c))

print(ans[0])