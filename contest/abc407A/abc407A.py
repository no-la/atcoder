import sys

input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())
t = A // B
if abs(t * B - A) < abs((t + 1) * B - A):
    print(t)
else:
    print(t + 1)
