import sys

input = lambda: sys.stdin.readline().rstrip()
X, Y, N = map(int, input().split())
print(min(X * N, Y * (N // 3) + X * (N % 3)))
