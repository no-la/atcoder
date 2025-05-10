import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = list(map(int, input().split()))

d = set()
for i, a in enumerate(A):
    d.add(a)
    if len(d) == M:
        print(N - i)
        exit()

print(0)
