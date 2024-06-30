N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

left = []
right = []
for i in range(N):
    if S[i]=="0":
        left.append(X[i])
    else:
        right.append(X[i])

left.sort()
right.sort()

# print(left)
# print(right)

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
ans = 0
for i in range(N):
    if S[i]=="1":
        from_ = bisect.bisect_left(left, X[i])
        to = bisect.bisect_right(left, X[i]+2*T)
        ans += abs(to-from_)
        # print(i, from_, to)
print(ans)
