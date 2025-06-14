import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())

A = list(range(1, N + 1))
offset = 0

for _ in range(Q):
    t, *others = map(int, input().split())
    if t == 1:
        p, x = others
        A[(p - 1 + offset) % N] = x
    elif t == 2:
        p = others[0]
        print(A[((p - 1 + offset) % N)])
    else:
        k = others[0]
        offset += k
