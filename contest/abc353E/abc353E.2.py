N = int(input())
S = input().split()

S.sort()


ans = 0

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for i in range(N-1):
    s = S[i]
    before = len(s)
    for j in range(len(s)):
        temp = bisect.bisect_right(S[:before], s[:j])
        ans += temp-i-1

print(ans)
