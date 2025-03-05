import sys

input = lambda: sys.stdin.readline().rstrip()

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

# 100C5

ans = 0
# 重複なし組み合わせ O(nCk)
import itertools
for l in itertools.combinations(A, 5):
    temp = 1
    for x in l:
        temp *= x
        temp %= P
    ans += temp == Q

print(ans)
