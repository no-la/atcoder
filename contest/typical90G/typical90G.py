import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for _ in range(Q):
    B = int(input())
    i = bisect.bisect_left(A, B)
    j = i - 1
    if j < 0:
        print(abs(A[i] - B))
    elif i == N:
        print(abs(A[j] - B))
    else:
        print(min(abs(A[i] - B), abs(A[j] - B)))
