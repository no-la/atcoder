import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

# 決め打ち二分探索
l, r = 0, N // 2 + 1
while l + 1 < r:  # [l, r)は可能性のある範囲
    c = (l + r) // 2
    a = 0
    b = -c
    for i in range(c):
        if A[a + i] * 2 > A[b + i]:
            break
    else:
        l = c
        continue
    r = c

print(l)
