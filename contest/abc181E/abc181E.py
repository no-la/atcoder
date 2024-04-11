N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
W.sort()

# (偶数番目の和)-(奇数番目の和)が最小になるような
# 自身の挿入箇所を探せばよい（偶奇だけ気にすればいい）

s1 = [0]*(N+2) # s1[i]: sum(H[:i:2])
s2 = [0]*(N+1) # s1[i]: sum(H[1:i:2]

for i in range(1, N+1):
    if i%2:
        s1[i] += s1[i-1]+H[i-1]
        s1[i+1] += s1[i]
    else:
        s2[i] += s2[i-1]+H[i-1]
        s2[i+1] += s2[i]
ans = 10**18

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for w in W:
    i = bisect.bisect_left(H, w)
    # ... <= H[i-1] < w <= H[i] <= ...
    if i==0:
        value = s1[-1]-s2[-1]-w
    elif i==N:
        value = s2[-1]+w-s1[-1]
    elif i%2:
        value = s2[i]+w-s1[i] + s1[-1]-s1[i]-(s2[-1]-s2[i])
    else:
        print(w, i, s1, s2)
        value = s2[i-1]-s1[i-1] + s1[-1]-s1[i-1]-(s2[-1]-s2[i-1]-w)
    ans = min(ans, value)
print(ans)
