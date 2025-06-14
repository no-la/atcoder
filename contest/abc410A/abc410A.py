import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = 0
for a in A:
    ans += K <= a

print(ans)
