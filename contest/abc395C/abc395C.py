import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
M = max(A) + 1
d = [[] for _ in range(M)]

for i, a in enumerate(A):
    d[a].append(i)

INF = N + 1
ans = INF

for l in d:
    for i in range(len(l) - 1):
        ans = min(ans, l[i + 1] - l[i] + 1)

print(ans if ans != INF else -1)
