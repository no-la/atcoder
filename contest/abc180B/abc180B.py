import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
X = list(map(int, input().split()))

import math

print(sum([abs(x) for x in X]))
print(math.sqrt(sum([x**2 for x in X])))
print(max([abs(x) for x in X]))
