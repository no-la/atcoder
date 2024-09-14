N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())

from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    d[X[i]] = P[i]

cor = [-10**10] + sorted(d.keys())
val = [d[k] for k in cor]

for i in range(N):
    val[i+1] += val[i]

# print(cor, val, sep="\n")
import bisect
for _ in range(Q):
    l, r = map(int, input().split())
    li = bisect.bisect_left(cor, l)
    ri = bisect.bisect_right(cor, r)

    ans = val[ri-1]-val[li-1]
    # print(li, ri)
    print(ans)

