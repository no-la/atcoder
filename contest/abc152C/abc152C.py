import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
P = list(map(int, input().split()))

x = N + 1
ans = 0
for p in P:
    ans += x > p
    x = min(x, p)

print(ans)
