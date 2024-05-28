N = int(input())
A = list(map(int, input().split()))

# j-i == A[i]+A[j] なる i<j を数える
# A[i]+i == -A[j]+j なる i<j を数える

d1 = [-A[i]+i for i in range(N)]
d2 = [A[i]+i for i in range(N)]
d1.sort()
d2.sort()

# print(d1)
# print(d2)

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
ans = 0
for v in d1: # v = A[i]+i
    l = bisect.bisect_left(d2, v) # j in [l, r), v = -A[j]+j
    r = bisect.bisect_right(d2,v)
    # print(v, l, r)
    count = r-l
    ans += count

print(ans)
