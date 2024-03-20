N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)

A.sort()
ans = 0
for i, a in enumerate(A):
    t = a
    while t<=A[-1]:
        d[t] += 1
        t += a

# print([(a, d[a]) for a in A])
print(sum([1 for a in A if d[a]==1]))