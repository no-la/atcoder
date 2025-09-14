import sys

input = lambda: sys.stdin.readline().rstrip()
X, C = map(int, input().split())
print((X // (1000 + C)) * 1000)
