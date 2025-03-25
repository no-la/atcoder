import sys

input = lambda: sys.stdin.readline().rstrip()
W, H = map(int, input().split())
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))

from collections import defaultdict
import bisect

count = defaultdict(int)

for i, x in enumerate(d):
    p, q = x
    pi = bisect.bisect_left(A, p)
    qi = bisect.bisect_left(B, q)
    count[(pi, qi)] += 1

m = min(count.values()) if len(count) == (len(A) + 1) * (len(B) + 1) else 0
M = max(count.values())
print(m, M)
