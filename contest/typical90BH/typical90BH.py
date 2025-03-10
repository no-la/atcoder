"""「連続とは限らない」を見落としてた"""

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

# 各要素から始まる単調増加列、単調減少列の最大長を尺取り法で調べる
asc_len = [1] * N
dsc_len = [1] * N

# >
right = 0
for left in range(N):
    right = max(right, left + 1)
    while right < N and A[right] < A[right - 1]:
        right += 1
    dsc_len[left] = max(dsc_len[left], right - left)
    # print(left, right)
    if left == right:
        right += 1

# print(dsc_len)

# <
left = N - 1
for right in range(N - 1, -1, -1):
    left = min(left, right - 1)
    while left >= 0 and A[left] < A[left + 1]:
        left -= 1
    asc_len[right] = max(asc_len[right], right - left)
    # print(left, right)
    if right == left:
        left -= 1

# print(asc_len)

ans = 1
for i in range(N):
    ans = max(ans, asc_len[i] + dsc_len[i] - 1)
    print(asc_len[i], dsc_len[i], "at", i)

print(ans)
