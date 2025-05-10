import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

d = 0
ans = 0
for a in A:
    ans += d * a
    d += a

print(ans)
