import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
print(sum([abs(a - b) for a, b in zip(A, B)]))
