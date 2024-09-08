N = int(input())
from collections import defaultdict
d = defaultdict(lambda: [(0, 0), (0, 0)])

for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        temp = d[p].copy()
        temp.append((e, i))
        temp.sort(reverse=True)
        d[p] = temp[:2]

ans = set()
has_no_change = 0
for v1, v2 in d.values():
    e1, i1 = v1
    e2, i2 = v2
    if e1==e2:
        has_no_change = 1
    elif e1>e2:
        ans.add(i1)

print(*d.items(), sep="\n")
print(len(ans)+has_no_change)
