N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

d = defaultdict(lambda: -1)
B = [0] * N
for i in range(N):
    B[i] = d[A[i]]
    d[A[i]] = i + 1
print(*B)
