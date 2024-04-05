N, Q = map(int, input().split())
R = list(map(int, input().split()))

# 累積和と二分探索？
R.sort()
d = [0]*(N+1) # d[i]: トナカイi匹が引けるそりの最大数
for i in range(1, N+1):
    d[i] = d[i-1] + R[i-1]

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for _ in range(Q):
    x = int(input())
    print(bisect.bisect_right(d, x)-1)