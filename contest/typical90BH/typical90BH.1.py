import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
INF = N + 1

d1 = [1] * N
d2 = [INF] * N
# d1[i]: 最後の要素がA[i]であるような単調増加列の最大長
# d2[i]: 長さがiであるような単調増加列の最終要素の最小値

e1 = [1] * N
e2 = [INF] * N
# e1[i]: 最初の要素がA[i]であるような単調減少列の最大長
# e2[i]: 長さがiであるような単調減少列の初項の最小値

for i, a in enumerate(A):
    j = bisect.bisect_left(d2, a)
    d2[j] = a
    d1[i] = j + 1

for i, a in enumerate(A[::-1]):
    j = bisect.bisect_left(e2, a)
    e2[j] = a
    e1[-i - 1] = j + 1

ans = 1
for i in range(N):
    ans = max(ans, d1[i] + e1[i] - 1)

print(ans)
# print(d1, e1, sep="\n")
