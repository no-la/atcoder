import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
A = list(map(int, input().split()))
offset = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        l, r = (x - offset - 1) % N, (y - offset - 1) % N
        A[l], A[r] = A[r], A[l]
    elif t == 2:
        offset += 1
    else:
        print(A[(x - offset - 1) % N])
    # print(A[-offset:], A[:-offset], sep="")
