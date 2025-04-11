import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

A.sort()

import bisect

ans = 0
for a in A:
    bi = bisect.bisect_right(A, a / 2)
    ans += bi

print(ans)
