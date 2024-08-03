N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

d = [0]*(N+1)
for i in range(N):
    d[i+1] = d[i] + A[i]

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
l, r = 0, M+1
while l<r-1:
    c = (l+r)//2
    i = bisect.bisect_left(A, c)
    temp = d[i] + c*(N-i)
    if temp<=M:
        l = c
    else:
        r = c

ans = l if l<max(A) else "infinite"
print(ans)


