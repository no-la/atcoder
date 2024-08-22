N, M = map(int, input().split())
A = list(map(int, input().split()))

# A = A+A

right = [0]
for a in A:
    right.append(right[-1]+a)

left = [right[-1]-r for r in reversed(right)]
right_mod = [r%M for r in right]
left_mod = [l%M for l in left]

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく

