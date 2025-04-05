import sys

input = lambda: sys.stdin.readline().rstrip()
A = int(input())
print(400 // A if 400 % A == 0 else -1)
