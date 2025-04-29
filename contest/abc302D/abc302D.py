import sys, bisect

input = lambda: sys.stdin.readline().rstrip()
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = -1
for i in range(N):
    j = bisect.bisect_right(B, A[i] + D) - 1
    temp = A[i] + B[j] if j >= 0 and abs(A[i] - B[j]) <= D else -1
    ans = max(ans, temp)

print(ans)
