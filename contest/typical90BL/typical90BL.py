import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i + 1] - A[i] for i in range(N - 1)]
s = sum([abs(b) for b in B])

# 階差数列とその絶対値の総和を持つ
for _ in range(Q):
    l, r, v = map(int, input().split())
    l, r = l - 1, r - 1
    if l > 0:
        s -= abs(B[l - 1])
        B[l - 1] += v
        s += abs(B[l - 1])
    if r < N - 1:
        s -= abs(B[r])
        B[r] -= v
        s += abs(B[r])

    print(s)
