import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = sum([abs(a - b) for a, b in zip(A, B)])
print("Yes" if K >= count and (K - count) % 2 == 0 else "No")
