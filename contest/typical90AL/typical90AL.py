import sys

input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())
INF = 10**18
import math

g = math.gcd(A, B)
ans = A * B // g
print(ans if ans <= INF else "Large")
