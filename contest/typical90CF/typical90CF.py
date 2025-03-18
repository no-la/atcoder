import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
S = input()

d = [[], []]
for i, s in enumerate(S):
    d[s == "o"].append(i)

import bisect

ans = 0
for l, s in enumerate(S):
    j = s != "o"
    ri = bisect.bisect_left(d[j], l)
    if ri < len(d[j]):
        r = d[j][ri]
        ans += N - r

print(ans)
