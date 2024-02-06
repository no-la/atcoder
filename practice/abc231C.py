N, Q = map(int, input().split())
A = list(map(int, input().split()))


A.sort(reverse=True)
B = A[::-1]
d = {A[0]:1} #身長がkey以上の生徒の数
before = -1
for i in range(1, N):
    if A[i]==before:
        d[A[i]] += 1
    else:
        d[A[i]] = d[A[i-1]]+1
        before = A[i]
ans = []
import bisect
for _ in range(Q):
    x = int(input())
    k = bisect.bisect_left(B, x)
    if k==N:
        ans.append("0")
    else:
        ans.append(str(d[B[k]]))
print("\n".join(ans))