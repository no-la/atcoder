import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
d = []
for _ in range(N):
    a, b = map(int, input().split())
    d.append(b)
    d.append(a - b)

d.sort(reverse=True)
print(sum(d[:K]))
