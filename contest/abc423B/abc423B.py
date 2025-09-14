import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
L = list(map(int, input().split()))

l = 0
while l < N and L[l] == 0:
    l += 1
r = N - 1
while r >= 0 and L[r] == 0:
    r -= 1


print(max(0, r - l))
